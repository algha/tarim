from app.modules.admin.core.menu import MenuItem, AdminMenu

class AdminMenus(AdminMenu):

    def menu(self):
        menus = []
        menus.append(
            MenuItem('Dashboard').setOrder(0)\
            .setIcon('fa-tachometer-alt')\
            .setActive('admin.main')\
            .setPermission('dashboard.access')\
            .setRoute('admin.main')\
            .setHead('Dashboard')
        )

        menus.append(
            MenuItem('Notification').setOrder(1)\
            .setIcon('fa-bell')\
            .setActive('admin.notification')\
            .setPermission('notification.access')\
            .setRoute('admin.notification')
        )

        menus.append(
            MenuItem('ToolBox').setOrder(2)\
            .setIcon('fa-toolbox')
            .setActive('admin.toolbox.*')\
            .setPermission('toolbox.access')\
            .setRoute('admin.toolbox.list')\
            .setDivier(True)
        )
        return menus
