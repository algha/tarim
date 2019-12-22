from .field import Field

class InputField(Field):

    template = 'fields/input.html'
    type = 'input'
    title = 'String'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)

    def input_type(self, type):
        self.set('type', type)
        return self

    def placeholder(self, placeholder):
        self.set('placeholder', placeholder)
        return self

    def initAttributes(self):
        self.attributes = {
            'value': None,
            'name': None,
            'placeholder': None,
            'type': 'text',
        }
