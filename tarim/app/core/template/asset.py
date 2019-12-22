
class Asset:

    def __init__(self):
        self.assets = {}
        self.module = ""

    @property
    def JAVASCRIPT(self):
        return "JAVASCRIPT"

    @property
    def STYLE(self):
        return "STYLE"

    def setModule(self, module):
        self.module = module
        return self

    def getAsset(self, module, asset):
        if module not in self.assets:
            self.assets[module] = {}

        if asset not in self.assets[module]:
            self.assets[module][asset] = []
        return self.assets[module][asset]

    def setAsset(self, module, asset, files):
        self.assets[self.module][asset] = files
        return self

    def getJS(self, module):
        return self.getAsset(module, self.JAVASCRIPT)

    def setJS(self, files):
        self.setAsset(self.module, self.JAVASCRIPT, files)
        return self

    def addJS(self, files):
        javascript = self.getJS(self.module)
        javascript.append(files)
        self.setJS(javascript)
        return self

    def getCSS(self, module):
        return self.getAsset(module, self.STYLE)

    def setCSS(self, files):
        self.setAsset(self.module, self.STYLE, files)
        return self

    def addCSS(self, files):
        style = self.getCSS(self.module)
        style.append(files)
        self.setCSS(style)
        return self

    def javascript(self, file):
        script = "<script src='{0}' type='text/javascript'></script>\n"
        script = script.format(file)
        return script

    def showJavascript(self, module):
        js = ''
        for _js in self.getJS(module):
            js += self.javascript(_js)
        return js

    def css(self, file):
        css = "<link rel='stylesheet' type='text/css' href='{0}'>\n"
        css = css.format(file)
        return css

    def showStyle(self, module):
        css = ''
        for _css in self.getCSS(module):
            css += self.css(_css)
        return css
