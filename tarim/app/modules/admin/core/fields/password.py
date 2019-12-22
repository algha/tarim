from .field import Field

class PasswordField(Field):

    template = 'fields/password.html'
    type = 'password'
    title = 'Password'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)

    def placeholder(self, placeholder):
        self.set('placeholder', placeholder)
        return self

    def initAttributes(self):
        self.attributes = {
            'value': None,
            'type': 'password'
        }
