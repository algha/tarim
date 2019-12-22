from flask import url_for

from app.modules.admin.core.layouts import Form, Table, TD
from app.modules.admin.core.fields import (InputField,
                                           SelectField,
                                           TextAreaField)

"""
    User form layout
    Add/Edit actions perform here
"""
class TypeListLayout(Table):

    data = 'types'

    def filters(self):
        return []

    def fields(self):
        return [
            TD('#').setRender(
                lambda item: self.clousureForID(item)
            ).setWidth(60),
            TD('Title','title'),
            TD('Slug','slug'),
            TD('Fields').setRender(
                lambda item: self.clousureForField(item)
            ),
            TD('Created at').setRender(
                lambda item: item.created_at.to_date_string()
            )
        ]

    def clousureForID(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.toolbox.type.edit', id=item.id), item.id)
        )

    def clousureForField(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.toolbox.field.list', id=item.id),
                        item.fields.count())
        )

"""
    User list layout
    List Data here
"""
class TypeEditLayout(Form):

    data = 'type'

    def fields(self):
        name = (
            InputField('title', 'Title')\
            .required()\
            .placeholder('Input your title')
        )

        slug = (
            InputField('slug', 'Slug')\
            .required()\
            .placeholder('Input your slug')
        )

        description = (
            TextAreaField('description', 'Description')\
            .placeholder('Input your description')
        )

        return [
            name, slug, description
        ]

    def validation(self):
        return {
            'title': 'required',
            'slug': 'required'
        }
