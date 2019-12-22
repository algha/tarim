from flask import url_for
from app.modules.admin.core.fields import SelectField

class TagField(SelectField):

    template = 'admin/fields/tags.html'
    type = 'tag'
    title = 'Tag'

    def __init__(self, name = None, label = None, post_type = None, **kwargs):
        super().__init__(name, label, **kwargs)
        self.options = {}

    def initAttributes(self):
        self.attributes = {
            'multiple': True,
            'name': 'tag'
        }

    def initDataAttributes(self):
        self.dataAttributes = {
            'url': url_for('admin.tag.search')
        }
