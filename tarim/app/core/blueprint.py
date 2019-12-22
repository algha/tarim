from flask import Blueprint, send_from_directory, current_app

class BaseBlueprint(Blueprint):

    def __init__(self, *args, **kwargs):
        super(BaseBlueprint, self).__init__(*args, **kwargs)
        self.built_in_routes()

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        super(BaseBlueprint, self).add_url_rule(rule,
                                                endpoint,
                                                view_func,
                                                **options)

    def add_blueprint(self, blueprint, **options):
        blueprint.name = self.name + '.' + blueprint.name

        blueprint.url_prefix = (
                (self.url_prefix or u"") +
                (options.get('url_prefix', blueprint.url_prefix) or u"")
        )
        if 'url_prefix' in options:
            del options['url_prefix']
        def deferred(state):
            state.app.register_blueprint(blueprint,
                                         url_prefix=blueprint.url_prefix,
                                         **options)
        self.record(deferred)

    def addView(self, view, **options):
        if hasattr(view, 'rules'):
            for key, value in view.rules().items():
                self.add_url_rule(value, view.endpoint,
                                  view.as_view(key), **options)
        else:
            self.add_url_rule(view.rule,
                              view.endpoint,
                              view.as_view(view.name),
                              methods = view.methods,
                              **options)

    def addScreen(self, screen, **options):
        screen.blueprint = self
        for rule in screen.rules():
            self.addScreenRule(rule, screen.as_view(rule.name),  **options)

    def addScreenRule(self, rule, view_func, **options):
        if rule.hasNative() or rule.hasSecondary():
            self.add_url_rule(rule.rule,
                              rule.endpoint,
                              view_func,
                              methods = rule.getMethodsOfSecondary(),
                              **options)
        if rule.hasOption():
            opt_rule = '{}/<path:method>'.format(rule.rule)
            self.add_url_rule(opt_rule,
                             rule.endpoint,
                             view_func,
                             methods = rule.methods,
                             **options)

    def built_in_routes(self):
        pass


class ModuleBlueprint(BaseBlueprint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class PluginBlueprint(Blueprint):
    pass
