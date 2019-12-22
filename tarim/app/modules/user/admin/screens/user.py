from flask import url_for, redirect, request, flash
from app.core.rule import Rule

from app.modules.admin.core.permission import MethodPermission
from app.modules.admin.core.screen import Screen
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.link import Link
from app.modules.admin.core.menu import MenuItem
from app.modules.user.models.user import User
from app.modules.user.models.role import Role

from ..layouts.user import UserListLayout, UserBaseEditLayout, UserInfoEditLayout

class UserListScreen(Screen):

    name = 'User'
    description = 'User List'

    permission = 'user.access'

    @staticmethod
    def rules():
        return [
            Rule('list', type = ['native'])
        ]

    def Query(self, **kwargs):
        users = User.all()
        return {'users': users}

    def Layout(self):
        return [
            UserListLayout()
        ]

    def CommandBar(self):
        links = [
            Link('Add New', url_for('admin.user.create')),
        ]
        return links

    def breadcrumb(self):
        return 'Users'


class UserEditScreen(Screen):

    name = 'User'
    description = 'User'

    permission = 'user.view'

    @staticmethod
    def rules():
        return [
            Rule('create', '/create','POST'),
            Rule('edit', '/<int:id>/edit','POST'),
        ]

    def Query(self, id = None):
        self.user = User.first_or_new(id=id)

        if id:
            role = self.user.roles.pluck('id').map(
                lambda id: str(id)
            ).serialize()
            self.user.setAttribute('role', role)

        return {'user': {'user': self.user, 'roles': Role.all().pluck('name', 'id')}}

    def Layout(self):
        return (
            Layout.addLayout('column', [UserBaseEditLayout(), UserInfoEditLayout()])
        )


    def CommandBar(self):
        links = []
        if hasattr(self.user, 'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return  links

    @MethodPermission('user.delete')
    def delete(self, id):
        user = User.find(id)
        if user is None:
            flash('User not found.', 'success')
        elif user.is_admin:
            flash('Admin can not be deleted', 'warning')
        else:
            flash('Successfully deleted.', 'success')
            user.delete()

        return redirect(url_for('admin.user.list'))

    @MethodPermission('user.edit')
    def save(self, id = None):
        user = User.first_or_new(id=id)
        baseform = UserBaseEditLayout(request.form, 'user')
        infoform = UserInfoEditLayout(request.form, 'user')

        if baseform.isValidated() == False or infoform.isValidated() == False:
            errors = '<br />'.join(baseform.getValidationError()+infoform.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))


        data = baseform.getFormData()
        if data['password'] == '':
            del data['password']
        else:
            data['password'] = user.set_password(data['password'])
        user.fill(data).save()

        roles = request.form.getlist('role[]')
        user.roles().sync(roles)

        flash('Successfully saved.', 'success')

        return redirect(url_for('admin.user.list'))

    """
    After this, coming with metadata
    """
    def parents(self):
        return [UserListScreen]

    def breadcrumb(self):
        if hasattr(self.user, 'id'):
            return 'Edit'
        else:
            return 'Create'
