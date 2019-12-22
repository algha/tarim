from flask import url_for, redirect, request, flash
from app.core.rule import Rule

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.link import Link
from app.modules.admin.core.layout import Layout
from app.modules.user.models.role import Role, Permission

from app.modules.admin.blueprint import Toolbox

from ..layouts.role import RoleListLayout, RoleEditLayout, PermissionsLayout

class RoleListScreen(Screen):

    name = 'Role'
    description = 'Role list'

    permission = 'role.access'

    @staticmethod
    def rules():
        return [
            Rule('list', '', type = ['native'])
        ]

    def Query(self, **kwargs):
        role = Role.all()
        return {'role': role}

    def Layout(self):
        return [
            RoleListLayout()
        ]

    def CommandBar(self):
        links = [
            Link('Add New', url_for('admin.toolbox.access.role.create')),
        ]
        return  links

    """
    After this, coming with metadata
    """
    def parents(self):
        return [Toolbox]

    def breadcrumb(self):
        return 'Roles'

class RoleEditScreen(Screen):

    name = 'Role'
    description = 'Role Edit'

    permission = 'permission.access'

    @staticmethod
    def rules():
        return [
            Rule('create', '/create', 'POST'),
            Rule('edit', '/<int:id>/edit', 'POST'),
        ]

    def Query(self, id = None):
        self.role = Role.first_or_new(id=id)
        permissions = Permission.order_by('sort', 'asc').get()
        actions = []
        if hasattr(self.role, 'actions'):
            actions = self.role.actions.pluck('id').to_json()
        permission = {
            'permissions' : permissions,
            'actions': actions
        }
        return {'role': self.role, 'permission' : permission}

    def Layout(self):
        return (
            Layout.addLayout('column', [RoleEditLayout(), PermissionsLayout()])
        )

    def CommandBar(self):
        links = []
        if hasattr(self.role,'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return  links


    def delete(self, id):
        Role.find(id).actions().detach()
        Role.destroy(id)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.toolbox.access.role.list'))

    def save(self, id = None):
        role = Role.first_or_new(id=id)
        form = RoleEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        role.fill(form.getFormData()).save()

        actions = request.form.getlist('action[]')
        role.actions().sync(actions)

        flash('Successfully deleted.', 'success')

        return redirect(url_for('admin.toolbox.access.role.list'))

    """
    After this, coming with metadata
    """

    def parents(self):
        return [Toolbox, RoleListScreen]

    def breadcrumb(self):
        if hasattr(self.role,'id'):
            return 'Edit'
        else:
            return 'Create'
