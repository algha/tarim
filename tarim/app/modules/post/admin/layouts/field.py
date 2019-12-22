from flask import url_for
from app import algha

from app.modules.admin.core.layouts import (Form,
                                            Table,
                                            TD,
                                            HorizontalLink,
                                            LinkItem)
from app.modules.admin.core.fields import (InputField,
                                           SelectField,
                                           TextAreaField,
                                           CodeField)
from app.modules.admin.core.link import Link





"""
    User form layout
    Add/Edit actions perform here
"""
class FieldListLayout(Table):

    data = 'fields'

    sortable_url = 'admin.toolbox.field.sort'

    def filters(self):
        return []

    def tableInfo(self):
        return 'this is test info'

    def buttonGroup(self):
        return [
            Link('Create field').loadModalAsync('getField',
                                                'asyncGetField',
                                                'saveField')
        ]

    def fields(self):
        type = self.getQuery('types').first(
            lambda item: item.isActive == True
        )

        return [
            TD('#').loadModalAsync('getField',
                                   'asyncGetField',
                                   'saveField',
                                   'id',
                                   'Edit'),
            TD('Title','title'),
            TD('Name','name'),
            TD('Type', 'field_type'),
            TD('Regex', 'regex'),
            TD('Place', 'place'),
            TD('Created at').setRender(
                lambda item: item.created_at.to_date_string()
            )
        ]

    def clousureForID(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.toolbox.field.edit',
                                id = item.content_type_id,
                                fid = item.id), item.id)
        )

    def clousureForField(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.toolbox.field.list', id = item.id),
                        item.fields.count())
        )


class TypeLinkLayout(HorizontalLink):

    data = 'types'
    name = 'Content Types'

    width = 'is-one-fifth'

    def items(self):
        items = []
        for type in self.getQuery():
            item = LinkItem(
                type.title,
                url_for('admin.toolbox.field.list',id=type.id),
                type.isActive
            )
            items.append(item)
        return items


class FieldEditLayout(Form):

    data = 'field'

    def fields(self):
        config = algha.getConfig('post')
        type = (
            SelectField('field_type', 'Field type')\
            .required()\
            .setOptions(config.field_types())
        )
        place = (
            SelectField('place', 'Place')\
            .setOptions({
                'main': 'Main',
                'side': 'Side'
            })
        )
        title = (
            InputField('title', 'Title')\
            .required()\
            .placeholder('Input your title')
        )
        name = (
            InputField('name', 'Name')\
            .required()\
            .placeholder('Input your Name')
        )
        show_in_table = (
            SelectField('show_in_table', 'Show in table')\
            .setOptions({0: 'No', 1 : 'Yes'})
        )
        is_required = (
            SelectField('is_required', 'Required')\
            .setOptions({
                '0': 'No',
                '1': 'Yes'
            })
        )
        regex = (
            InputField('regex', 'Regex')\
            .placeholder('Example: required|min:2|max:10')
        )
        dataattr = (
            CodeField('dataattr', 'Data Attr')
        )
        default_value = (
            TextAreaField('default_value', 'Default Value')\
            .placeholder('Input your Default Value')
        )

        return [
            place, type, title, name, show_in_table,
            is_required, regex, dataattr, default_value
        ]

    def validation(self):
        return {
            'title': 'required',
            'name': 'required',
            'place': 'required',
            'field_type': 'required'
        }
