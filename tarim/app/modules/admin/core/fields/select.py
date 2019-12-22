from .field import Field

class SelectField(Field):

    template = 'fields/select.html'
    type = 'select'
    title = 'Select'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)
        self.options = {}

    def setOptions(self, options):
        self.options = options
        return self

    def setMultiple(self):
        self.set('multiple', True)
        return self

    def isMultiple(self):
        if self.get('multiple'):
            return True
        return False

    def getName(self):
        name = self.get('name')
        if self.isMultiple():
            name = '{}[]'.format(name)
        return name

    def getValue(self):
        value = getattr(self, 'value', None)
        if value:
            return value
        return ''

    def isSelected(self, key):
        value = self.getValue()
        if isinstance(value, str):
            value = [value]
        if isinstance(value, int):
            value = [str(value)]
        if isinstance(key, int):
            key = str(key)
        if key in value:
            return 'selected'
        return ''

    def initAttributes(self):
        self.attributes = {
            'multiple': None
        }
