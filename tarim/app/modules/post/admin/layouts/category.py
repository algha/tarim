from flask import url_for

from app.modules.admin.core.layouts import Form, Table, TD
from app.modules.admin.core.fields import (InputField,
                                           SelectField,
                                           TextAreaField)

"""
    User form layout
    Add/Edit actions perform here
"""
class CategoryListLayout(Table):

    data = 'categories'

    def filters(self):
        return []

    def fields(self):
        return [
            TD('#').setRender(
                lambda item: self.clousureForID(item)
            ).setWidth(60),
            TD('Title','title'),
            TD('Slug','slug'),
            TD('Type','type'),
            TD('Created at').setRender(
                lambda item: item.created_at.to_date_string()
            )
        ]

    def clousureForID(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.category.edit', id=item.id), item.id)
        )


"""
    User list layout
    List Data here
"""
class CategoryEditLayout(Form):

    data = 'category'

    def fields(self):
        name = (
            InputField('title', 'Title')\
            .required()\
            .placeholder('Input your title')
        )

        type = (
            SelectField('type', 'Type')\
            .setOptions(self.getQuery().types)
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
            name, type, slug, description
        ]

    def validation(self):
        return {
            'title': 'required',
            'type': 'type',
            'slug': 'required',
        }
