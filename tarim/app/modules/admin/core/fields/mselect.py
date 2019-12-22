from .select import SelectField

class MSelectField(SelectField):

    type = 'mselect'
    title = 'Multi Select'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)
        self.setMultiple()
