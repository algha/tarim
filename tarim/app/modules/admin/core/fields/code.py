from .field import Field

class CodeField(Field):

    template = 'fields/code.html'
    type = 'code'
    title = 'Code'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)

    def getValue(self):
        value = getattr(self, 'value', None)
        if value:
            return value
        return ''

    def initAttributes(self):
        self.attributes = {
            'type': 'text',
            'autocomplete': 'off'
        }

    def initDataAttributes(self):
        self.dataAttributes = {
            'language': "js",
            'line-numbers': "true",
            'default-Theme': "true",
            'height': 300
        }

    def dataAttrPrefix(self):
        return 'data-fields--code'
