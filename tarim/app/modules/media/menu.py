from app.modules.admin.core.menu import MenuItem, AdminMenu

class AdminMenus(AdminMenu):

    def menu(self):
        menus = []
        menus.append(
            MenuItem('Media')\
            .setOrder(1)
            .setRoute('admin.media.list')\
            .setActive('admin.media.*')\
            .setIcon('fa-images')\
            .setPermission('media.access')
        )

        return menus

    def toolbox(self):
        menus = []
        media = MenuItem('Media')\
                .setIcon('fa-images')\
                .setPermission('media.access')

        media.addChild([
            MenuItem('Media')\
            .setRoute('admin.media.list')\
            .setIcon('fa-images')\
            .setPermission('media.access')
        ])
        menus.append(media)
        return menus
