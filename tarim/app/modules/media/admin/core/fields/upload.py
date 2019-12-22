from app.modules.admin.core.fields import Field

class UploadField(Field):

    template = 'admin/fields/upload.html'
    type = 'upload'
    title = 'Upload'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)

    def setValues(self, values):
        self.values = values

    def getValue(self):
        value = getattr(self, 'value', None)
        if value:
            return value
        return ''

    def getName(self):
        name = self.get('name')
        name = '{}[]'.format(name)
        return name
