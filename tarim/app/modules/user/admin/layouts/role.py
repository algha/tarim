from flask import url_for

from app.modules.admin.core.layouts import Form, Table, TD
from app.modules.admin.core.fields import (InputField,
                                           TextAreaField,
                                           SelectField,
                                           CheckBoxField,
                                           LabelField)

class RoleListLayout(Table):

    data = 'role'

    def filters(self):
        return []

    def fields(self):
        return [
            TD('#').setRender(
                lambda item: self.clousureForID(item)
            ).setWidth(60),
            TD('Name','name'),
            TD('Slug','slug'),
            TD('Created at').setRender(
                lambda item: item.created_at.to_date_string()
            )
        ]

    def clousureForID(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.toolbox.access.role.edit', id=item.id), item.id)
            )


class RoleEditLayout(Form):

    data = 'role'
    name = 'Role'

    width = 'is-one-third'

    def fields(self):
        name = (
            InputField('name', 'Name')\
            .required()\
            .placeholder('Input your name')
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
        return [name, slug, description]

    def validation(self):
        return {
            'name': 'required',
            'slug': 'required'
        }


class PermissionsLayout(Form):

    data = 'permission'
    name = 'Permission'


    def fields(self):
        fields = []
        action = self.getChild('actions')

        for permission in self.getChild('permissions'):
            actions = permission.actions.pluck('name', 'id')
            checkbox = CheckBoxField().setLabel(permission.name)\
                                      .setValues(actions)\
                                      .setName('action[]')\
                                      .setChecked(action)
            fields.append(checkbox)
        return fields

    def validation(self):
        return {
            'name': 'required',
            'slug': 'required'
        }
