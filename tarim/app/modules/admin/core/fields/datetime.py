from .field import Field

class DateTimeField(Field):

    template = 'fields/datetime.html'
    type = 'datetime'
    title = 'DateTime'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)


    def initAttributes(self):
        self.attributes = {
            'value': None,
            'type': 'text',
            'autocomplete': 'off'
        }

    def initDataAttributes(self):
        self.dataAttributes = {
            'enable-time': "true",
            'time_24hr': "true",
            'allow-input': "false",
            'date-format': "Y-m-d h:i:s"
        }

    def dataAttrPrefix(self):
        return 'data-fields--datetime'
