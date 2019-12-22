from flask import url_for
from app.modules.admin.core.fields import Field

class PictureField(Field):

    template = 'admin/fields/picture.html'
    type = 'picture'
    title = 'Picture'

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(name, label, **kwargs)


    def getValue(self):
        value = getattr(self, 'value', None)
        if value:
            return value
        return ''

    def initDataAttributes(self):
        self.dataAttributes = {
            'url': url_for('admin.media.upload')
        }

    def setFrame(self, w = None, h = None):
        if w is not None:
            self.setData("width", w)
        if h is not None:
            self.setData("height", h)
        return self

    def setSquare(self, w):
        self.setFrame(w, w)
        return self

    def setRound(self):
        self.setData("rounded", "rounded")
        return self

    def setLock(self):
        self.setData("lock", "lock")
        return self
