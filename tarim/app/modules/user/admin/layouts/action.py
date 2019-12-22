from flask import url_for

from app.modules.admin.core.layouts import Form, Table, TD
from app.modules.admin.core.fields import (InputField,
                                           TextAreaField,
                                           SelectField,
                                           CheckBoxField)

class ActionListLayout(Table):

    data = 'action'

    def filters(self):
        return []

    def fields(self):

        return [
            TD('#').setRender(
                lambda item: self.clousureForID(item)
            ).setWidth(60),
            TD('Name','name'),
            TD('Slug','slug'),
            TD('Permission').setRender(
                lambda item: item.permission.name
            ),
            TD('Created at').setRender(
                lambda item: item.created_at.to_date_string()
            )
        ]

    def clousureForID(self, item):
        url = url_for('admin.toolbox.access.action.edit',
                      id = item.id,
                      permission_id = item.permission.id )
        return (
            '<a href="{}">{}</a>'.\
                format(url, item.id)
        )

class ActionEditLayout(Form):

    data = 'action'
    name = 'action'

    def fields(self):
        name = (
            InputField('name', 'Name')\
            .required()\
            .placeholder('Input your name')
        )
        slug = (
            InputField('slug', 'Slug')\
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
            'name': 'required',
            'slug': 'required'
        }
