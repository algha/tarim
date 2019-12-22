from flask import url_for

from app.modules.admin.core.layouts import Form, Table, TD
from app.modules.admin.core.fields import (InputField,
                                           TextAreaField,
                                           SelectField,
                                           CheckBoxField)
from app.modules.admin.core.link import Link


class PermissionListLayout(Table):

    data = 'permission'

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
            ),
            TD('Action').setRender(
                lambda item: self.clousureForAction(item)
            )
        ]

    def clousureForID(self, item):
        return (
            '<a href="{}">EDIT</a>'.\
                format(url_for('admin.toolbox.access.permission.edit', id=item.id))
        )

    def clousureForAction(self, item):

        define_action = Link(
            'Define Action',
            url_for('admin.toolbox.access.action.create',permission_id=item.id)
        ).setIcon('fa-plus')

        delete = Link(
            'Delete',
            url_for('admin.toolbox.access.permission.list_delete',id=item.id)
        ).setIcon('fa-trash-alt')\
         .setAjaxMethod('DELETE')\
         .setConfirm('Do you really delete?')

        edit = Link(
            'Edit',
            url_for('admin.toolbox.access.permission.edit',id=item.id)
        ).setIcon('fa-edit')

        link = Link('Actions', '#')
        link.appendChildren([define_action, delete, edit])
        return link.build()

class PermissionEditLayout(Form):

    data = 'permission'
    name = 'permission'

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
