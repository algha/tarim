from .field import Field

class TextAreaField(Field):

    template = 'fields/textarea.html'
    type = 'text'
    title = 'Text'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)

    def placeholder(self, placeholder):
        self.set('placeholder', placeholder)
        return self

    def getValue(self):
        value = getattr(self, 'value', None)
        if value:
            return value
        return ''

    def initAttributes(self):
        self.attributes = {
            'placeholder': None
        }
