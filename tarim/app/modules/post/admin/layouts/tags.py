from flask import url_for

from app.modules.admin.core.layouts import Form, Table, TD
from app.modules.admin.core.fields import (InputField,
                                           SelectField,
                                           TextAreaField)

"""
    User form layout
    Add/Edit actions perform here
"""
class TagsListLayout(Table):

    data = 'tags'

    def filters(self):
        return []

    def fields(self):
        return [
            TD('#').setRender(
                lambda item: self.clousureForID(item)
            ).setWidth(60),
            TD('Title','title'),
            TD('Slug','slug'),
            TD('Type', 'type'),
            TD('Count', 'count')
        ]

    def clousureForID(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.tag.edit', id=item.id), item.id)
        )


"""
    User list layout
    List Data here
"""
class TagEditLayout(Form):

    data = 'tag'

    def fields(self):
        name = (
            InputField('name', 'Name')\
            .required()\
            .placeholder('Input Name')
        )

        slug = (
            InputField('slug', 'Slug')\
            .required()\
            .placeholder('Input your slug')
        )

        return [
            name, slug
        ]

    def validation(self):
        return {
            'name': 'required',
            'slug': 'required'
        }
