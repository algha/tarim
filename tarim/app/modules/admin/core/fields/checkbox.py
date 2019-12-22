from .field import Field

class CheckBoxField(Field):

    template = 'fields/checkbox.html'
    type = 'checkbox'
    title = 'Checkbox'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)
        self.values = {}
        self.checked = []

    def setValues(self, values):
        self.values = values
        return self

    def getName(self):
        name = self.get('name')
        name = '{}[]'.format(name)
        return name

    def setChecked(self, checked):
        self.checked = checked
        return self

    def isChecked(self, key):
        if str(key) in self.checked:
            return "checked"
        return ''
