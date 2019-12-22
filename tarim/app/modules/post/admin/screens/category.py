from flask import url_for, redirect, request, flash
from app.core.rule import Rule

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.link import Link

from ..layouts.category import (CategoryListLayout,
                                CategoryEditLayout)

from app.modules.post.models.category import Category
from app.modules.post.models.content_type import ContentType

class CategoryList(Screen):

    name = 'Category'
    description = 'Category List'

    permission = 'category.access'

    @staticmethod
    def rules():
        return [
            Rule('list', type = ['native'])
        ]

    def Query(self, **kwargs):
        categories = Category.order_by('created_at','desc').get()
        return {'categories':categories}

    def Layout(self):
        layouts = [
            CategoryListLayout
        ]
        return layouts

    def CommandBar(self):
        links = [
            Link('Create',url_for('admin.category.create'))
        ]
        return links

    def breadcrumb(self):
        return 'Categories'


class CategoryEdit(Screen):

    name = 'Category'
    description = 'Category Edit'

    permission = 'category.view'

    @staticmethod
    def rules():
        return [
            Rule('create', '/create', 'POST'),
            Rule('edit', '/<id>/edit', 'POST')
        ]

    def Query(self, id = None, **kwargs):

        content_types = ContentType.where_has('fields',
            lambda q: q.where('field_type', 'category')
        ).get().pluck('title', 'slug')

        self.category = category = Category.first_or_new(id=id)
        category.setAttribute('types',content_types)

        return {'category':category}

    def Layout(self):
        layouts = [
            CategoryEditLayout
        ]
        return layouts

    def CommandBar(self):
        links = []
        if hasattr(self.category, 'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return links


    def delete(self, id):
        Category.destroy(id)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.category.list'))

    def save(self, id = None, **kwargs):
        category = Category.first_or_new(id=id)

        form = CategoryEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        category.fill(form.getFormData()).save()

        flash('Successfully saved.', 'success')

        return redirect(url_for('admin.category.list', type=type))

    def parents(self):
        return [CategoryList]

    def breadcrumb(self):
        if hasattr(self.category, 'id'):
            return 'Edit'
        return 'Create'
