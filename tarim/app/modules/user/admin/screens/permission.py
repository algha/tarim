from flask import url_for, redirect, request, flash
from app.core.rule import Rule

from app.modules.user.models.role import Permission
from app.modules.admin.core.screen import Screen
from app.modules.admin.core.link import Link
from app.modules.admin.core.layout import Layout

from app.modules.admin.blueprint import Toolbox

from ..layouts.permission import PermissionListLayout, PermissionEditLayout

class PermissionListScreen(Screen):

    name = 'Permission'
    description = 'Permission list'

    permission = 'permission.access'

    @staticmethod
    def rules():
        return [
            Rule('list', '', type = ['native']),
            Rule('list_delete', '/<id>/delete', 'DELETE', method = 'delete')
        ]

    def Query(self, **kwargs):
        permissions = Permission.order_by('sort', 'asc').get()
        return {'permission': permissions}

    def Layout(self):
        return [
            PermissionListLayout()
        ]

    def CommandBar(self):
        links = [
            Link('Add New', url_for('admin.toolbox.access.permission.create')),
        ]
        return  links

    """
    # after this will be performed actions
    """
    def delete(self, id):
        Permission.destroy(id)
        return 'deleted'

    """
    After this, coming with metadata
    """
    def parents(self):
        return [Toolbox]

    def breadcrumb(self):
        return 'Permissions'

class PermissionEditScreen(Screen):

    name = 'Permission'
    description = 'Permission Edit'

    permission = 'permission.access'

    @staticmethod
    def rules():
        return [
            Rule('create', '/create', 'POST'),
            Rule('edit', '/<int:id>/edit', 'POST'),
        ]

    def Query(self, id = None):
        self.permission = Permission.first_or_new(id=id)
        return {'permission': self.permission}

    def Layout(self):
        layouts = [
            PermissionEditLayout
        ]
        return layouts

    def CommandBar(self):
        links = []
        if hasattr(self.permission, 'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return  links

    """
    # after this will be performed actions
    """
    def delete(self, id):
        Permission.destroy(id)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.toolbox.access.permission.list'))

    def save(self, id = None):
        permission = Permission.first_or_new(id=id)
        form = PermissionEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        permission.fill(form.getFormData()).save()

        flash('Successfully deleted.', 'success')

        return redirect(url_for('admin.toolbox.access.permission.list'))

    """
    After this, coming with metadata
    """
    def parents(self):
        return [Toolbox, PermissionListScreen]

    def breadcrumb(self):
        if hasattr(self.permission, 'id'):
            return 'Edit'
        else:
            return 'Create'
