from flask import url_for, redirect, request, flash
from app.core.rule import Rule

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.link import Link

from app.modules.admin.blueprint import Toolbox

from app.modules.post.models.content_type import ContentType
from ..layouts.type import TypeListLayout, TypeEditLayout


class TypeList(Screen):

    name = 'Content Type'
    description = 'Content Type Builder'

    permission = 'content_type.access'

    @staticmethod
    def rules():
        return [
            Rule('list', type = ['native'])
        ]

    def Query(self, **kwargs):
        types = ContentType.order_by('created_at','desc').get()
        return {'types':types}

    def Layout(self):
        return [TypeListLayout()]

    def CommandBar(self):
        links = [
            Link('Add New', url_for('admin.toolbox.type.create')),
        ]
        return links

    def parents(self):
        return [Toolbox]

    def breadcrumb(self):
        return 'Content Builder'

class TypeEdit(Screen):

    name = 'Content Type'
    description = 'Content Type Edit'

    permission = 'content_type.view'

    @staticmethod
    def rules():
        return [
            Rule('create', '/create', 'POST'),
            Rule('edit', '/<id>/edit', 'POST')
        ]

    def Query(self, id = None, **kwargs):
        self.type = type = ContentType.first_or_new(id=id)
        return {'type':type}

    def Layout(self):
        return [TypeEditLayout()]

    def CommandBar(self):
        links = []
        if hasattr(self.type, 'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return links

    def delete(self, id):
        ContentType.destroy(id)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.toolbox.type.list'))

    def save(self, id = None, **kwargs):
        type = ContentType.first_or_new(id=id)
        form = TypeEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        type.fill(form.getFormData()).save()
        flash('Successfully saved.', 'success')
        return redirect(url_for('admin.toolbox.type.list'))

    def parents(self):
        return [Toolbox, TypeList]

    def breadcrumb(self):
        if hasattr(self.type, 'id'):
            return 'Edit'
        return 'Create'
