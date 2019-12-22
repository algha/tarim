from importlib import import_module

from .utils.processor import ContextProcessor
from .utils.func import *
from .template.asset import Asset

def getModule(module):
    package = '{}.config'.format(module)
    return import_module(package)

def getConfig(module):
    module = getModule(module)
    try:
        return getattr(module,'Config')
    except:
        raise('{} not found'.format(module))

class Algha(object):

    def __init__(self, app = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.asset = Asset()
        self.moduleRegister()
        self.registerUtils()

    def getModules(self):
        config = self.app.config['ALGHA_MODULES']
        if config:
            return config
        return []

    def getConfigs(self):
        configs = []
        modules = self.getModules()
        for module in modules:
            configs.append(getConfig(module))
        return configs

    def getConfig(self, key):
        for config in self.getConfigs():
            if config.key == key:
                return config
        return None

    def getBlueprint(self, config, key = None):
        config = self.getConfig(config)
        if key is None:
            return config.blueprints()
        return config.getBlueprint(key)

    def getModel(self, config, key = None):
        config = self.getConfig(config)
        if key is None:
            return config._models()
        return config.getModel(key)

    def moduleRegister(self):
        for config in self.getConfigs():
            config.entryPoint(self)

        for config in self.getConfigs():
            config.register_blueprints()

    def getFields(self):
        fields = []
        for config in self.getConfigs():
            fields.extend(config.fields())
        return fields

    def registerUtils(self):
        self.processor('func', 'to_string', to_string)
        self.processor('var', 'asset', self.asset)

    def processor(self, type, key, value):
        processor = ContextProcessor(self.app)
        if type == "func":
            processor.injectFuncs(key, value)
        if type == 'var':
            processor.injectVaribles(key, value)
