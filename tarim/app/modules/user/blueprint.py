from app.core.blueprint import ModuleBlueprint
from .admin.screens.user import (UserListScreen,
                                 UserEditScreen)
from .admin.screens.role import (RoleListScreen,
                                 RoleEditScreen)
from .admin.screens.permission import (PermissionListScreen,
                                       PermissionEditScreen)
from .admin.screens.action import (ActionListScreen,
                                   ActionEditScreen)

user = ModuleBlueprint('user',__name__, url_prefix = '/users')
user.addScreen(UserListScreen)
user.addScreen(UserEditScreen)

access = ModuleBlueprint('access',__name__, url_prefix = '/access')

role = ModuleBlueprint('role',__name__, url_prefix = '/role')
role.addScreen(RoleListScreen)
role.addScreen(RoleEditScreen)

permission = ModuleBlueprint('permission',__name__, url_prefix = '/permission')
permission.addScreen(PermissionListScreen)
permission.addScreen(PermissionEditScreen)

action = ModuleBlueprint('action',__name__, url_prefix = '/action')
action.addScreen(ActionListScreen)
action.addScreen(ActionEditScreen)
