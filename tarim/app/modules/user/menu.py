from app.modules.admin.core.menu import MenuItem, AdminMenu

class AdminMenus(AdminMenu):

    def menu(self):
        menus = []
        menus.append(
            MenuItem('Users')\
            .setOrder(10)\
            .setRoute('admin.user.list')\
            .setActive('admin.user.*')\
            .setIcon('fa-users')\
            .setPermission('user.access')\
            .setHead('User')
        )

        return menus

    def toolbox(self):
        menus = []
        permissions = MenuItem('Permissions').setIcon('fa-user-circle')
        permissions.addChild([
            MenuItem('Roles')\
            .setRoute('admin.toolbox.access.role.list')\
            .setIcon('fa-universal-access')
            .setPermission('role.access')\
            .setParent(permissions),

            MenuItem('Permissions')\
            .setRoute('admin.toolbox.access.permission.list')\
            .setIcon('fa-universal-access')\
            .setPermission('permission.access')\
            .setParent(permissions),

            MenuItem('Actions')\
            .setRoute('admin.toolbox.access.action.list')\
            .setIcon('fa-universal-access')\
            .setPermission('action.access')\
            .setParent(permissions)
        ])
        menus.append(permissions)
        return menus
