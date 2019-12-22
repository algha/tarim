class ContextProcessor:

    def __init__(self, app):
        self.app = app

    def injectVaribles(self, key, value):
        app = self.app
        @app.context_processor
        def var():
            return {key:value}


    def injectFuncs(self, key, func):
        app = self.app
        @app.context_processor
        def funcs():
            return {key:func}
