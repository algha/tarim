from flask import url_for, request, redirect, flash
from app.core.rule import Rule
from app.modules.user.models.role import Action, Permission
from app.modules.admin.core.screen import Screen
from app.modules.admin.core.link import Link
from app.modules.admin.core.layout import Layout

from app.modules.admin.blueprint import Toolbox

from ..layouts.action import ActionListLayout, ActionEditLayout
from .permission import PermissionListScreen

class ActionListScreen(Screen):

    name = 'Action'
    description = 'Action list'

    permission = 'action.access'

    @staticmethod
    def rules():
        return [
            Rule('list', '', type = ['native'])
        ]

    def Query(self, **kwargs):
        actions = Action.order_by('slug').get()
        return {'action': actions}

    def Layout(self):
        return [
            ActionListLayout()
        ]

    def CommandBar(self):
        return  []

    """
    After this, coming with metadata
    """
    def parents(self):
        return [Toolbox]

    def breadcrumb(self):
        return 'Actions'

class ActionEditScreen(Screen):

    name = 'Action'
    description = 'Action Edit'

    permission = 'action.access'

    @staticmethod
    def rules():
        return [
            Rule('create','/create/<permission_id>/permission','POST'),
            Rule('edit', '/<int:id>/edit/<permission_id>/permission', 'POST')
        ]

    def Query(self, id = None, permission_id = None):
        self.permission_id = permission_id
        self.action = Action.first_or_new(id=id)
        return {'action': self.action}

    def Layout(self):
        layouts = [
            Layout.addLayout('column', [ActionEditLayout()]),
        ]
        return layouts

    def CommandBar(self):
        links = []
        if hasattr(self.action, 'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return  links

    """
    # after this will be performed actions
    """
    def delete(self, id, permission_id = None):
        Action.destroy(id)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.toolbox.access.permission.list'))

    def save(self, id = None, permission_id = None):
        permission = Permission.find(permission_id)
        if not permission:
            return redirect(request.url.replace('/save',''))

        action = Action.first_or_new(id=id)
        form = ActionEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        data = form.getFormData()
        data['permission_id'] = permission.id
        action.fill(data).save()

        flash('Successfully deleted.', 'success')

        return redirect(url_for('admn.access.action.list'))

    """
    After this, coming with metadata
    """
    def parents(self):
        if self.permission_id is not None:
            return [Toolbox, PermissionListScreen, ActionListScreen]
        return [Toolbox, ActionListScreen]

    def breadcrumb(self):
        if hasattr(self.action, 'id'):
            return 'Edit'
        else:
            return 'Create'
