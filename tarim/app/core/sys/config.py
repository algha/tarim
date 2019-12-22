class ConfigBase(object):

    name = ''
    key = ''

    @classmethod
    def entryPoint(cls, algha):
        cls.algha = algha

    @classmethod
    def blueprints(cls):
        return {}

    @classmethod
    def register_blueprints(cls):
        for key, blueprint in cls.blueprints().items():
            cls.algha.app.register_blueprint(blueprint)

    @classmethod
    def _blueprints(cls):
        return {}

    @classmethod
    def getBlueprint(cls, key):
        blueprints = cls._blueprints()
        if key in blueprints:
            return blueprints[key]
        return None

    @classmethod
    def _models(cls):
        return {}

    @classmethod
    def getModel(cls, key):
        models = cls._models()
        if key in models:
            return models[key]
        return None

    @classmethod
    def fields(cls):
        return []

    @classmethod
    def adminMenu(cls):
        return None
