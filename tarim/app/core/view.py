from flask.views import View
from .utils.exception import InvalidUsage

class BaseView(View):

    rule = ''
    name = ''
    methods = ['GET']
    endpoint = None
    template = None

    def dispatch_request(self, *args ,**kwargs):
        return self.get(*args, **kwargs)

    def get(self, *args, **kwargs):
        return NotImplementedError()

    def getTemplate(self, **kwargs):
        if self.template is None:
            raise InvalidUsage('Template property is none', 410)

        return self.template.render(**kwargs)

    def render(self, template, **kwargs):
        return self.template.render(template, **kwargs)
