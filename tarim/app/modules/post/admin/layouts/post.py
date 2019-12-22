from flask import url_for
from app import algha

from app.modules.admin.core.layouts import Form, Table, TD

from ..core.field import FieldsList
"""
    User form layout
    Add/Edit actions perform here
"""
class PostListLayout(Table):

    data = 'posts'

    def filters(self):
        return []

    def fields(self):
        _fields = self.getQuery('fields')

        fields = []

        id = TD('#').setRender(
            lambda item: self.clousureForID(item)
        ).setWidth(60)
        fields.append(id)

        author = TD('Author').setRender(
            lambda item: item.user.name
        )
        fields.append(author)

        for field in _fields:
            _field = TD(field.title, field.name)
            fields.append(_field)

        click = TD('click').setRender(
            lambda item: item.click
        )
        fields.append(click)

        updated_at = TD('Updated at').setRender(
            lambda item: item.updated_at.to_date_string()
        )
        fields.append(updated_at)

        created_at = TD('Created at').setRender(
            lambda item: item.created_at.to_date_string()
        )
        fields.append(created_at)

        return fields

    def clousureForID(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(
                    url_for('admin.post.edit', type=item.type, id=item.id),
                    item.id
                )
        )


"""
    User list layout
    List Data here
"""

class PostForm(Form):

    place = None

    def __init__(self, validationFields = None, **kwargs):
        super().__init__(**kwargs)
        self.validationFields = validationFields

    def fields(self):
        fields = []

        fieldsTypeList = FieldsList()
        fieldsData = self.getQuery('fields').filter(
            lambda item: item.place == self.place
        ).all()
        config = algha.getConfig('post')
        for field in fieldsData:
            fieldObject = fieldsTypeList.getFieldObject(field.field_type)
            fieldObject = fieldObject(field.name, field.title,
                                      post_type = field.contentType.slug)
            fieldObject.required(field.is_required==1)
            fieldObject.parseDataAttr(field.dataattr)
            fields.append(fieldObject)

        return fields

    def validation(self):
        validations = {}
        for field in self.validationFields:
            validations[field.name] = field.regex
        return validations

class PostEditMainLayout(PostForm):

    data = 'post'
    place = 'main'


class PostEditSideLayout(PostForm):

    data = 'post'
    place = 'side'

    width = 'is-one-fifth'
