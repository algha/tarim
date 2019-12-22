from .field import Field

class LabelField(Field):

    template = 'fields/label.html'
    type = 'label'
    title = 'Label'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)
