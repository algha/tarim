from .field import Field

class TinyMCEField(Field):

    template = 'fields/tinymce.html'
    type = 'tinymce'
    title = 'TinyMCE'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)

    def getValue(self):
        value = getattr(self, 'value', None)
        if value:
            return value
        return ''

    def initAttributes(self):
        self.attributes = {
            'type': 'hidden'
        }

    def initDataAttributes(self):
        self.dataAttributes = {
            'theme': "modern", #inlite|modern
            'height': '150'
        }
