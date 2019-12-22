from orator.orm import belongs_to_many, belongs_to, has_many
from app.core.model import Model

class Role(Model):

    __table__ = 'roles'

    __fillable__ = [
        'name',
        'slug',
        'description'
    ]

    @belongs_to_many
    def users(self):
        from .user import User
        return User

    @belongs_to_many('role_action')
    def actions(self):
        return Action

class Permission(Model):

    __table__ = 'permissions'

    __fillable__ = [
        'name',
        'slug',
        'description',
        'sort'
    ]

    @has_many
    def actions(self):
        return Action

class Action(Model):

    __table__ = 'actions'

    __fillable__ = [
        'permission_id',
        'name',
        'slug',
        'description'
    ]

    @belongs_to
    def permission(self):
        return Permission
