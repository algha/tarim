from app.core.sys.config import ConfigBase
from .blueprint import user, permission, role, action, access

from .models.role import Role, Permission, Action
from .models.user import User

from .menu import AdminMenus

class Config(ConfigBase):

    key = 'user'

    @classmethod
    def entryPoint(cls, algha):
        admin = algha.getBlueprint('admin', 'admin')
        admin.add_blueprint(user)

        toolbox = algha.getBlueprint('admin', 'toolbox')
        toolbox.add_blueprint(access)

        access.add_blueprint(permission)
        access.add_blueprint(role)
        access.add_blueprint(action)

    @classmethod
    def adminMenu(cls):
        return AdminMenus()

    @classmethod
    def _models(cls):
        return {
            'user': User,
            'role': Role,
            'permission': Permission,
            'action': Action
        }
