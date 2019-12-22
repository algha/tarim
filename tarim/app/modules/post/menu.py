from app.modules.admin.core.menu import MenuItem, AdminMenu
from .models.content_type import ContentType
from flask import url_for

class AdminMenus(AdminMenu):

    def menu(self):
        menus = []
        PostTypes = ContentType.get()
        for index,type in enumerate(PostTypes):
            route = url_for('admin.post.list', type = type.slug)
            menu = MenuItem(type.title)\
                   .setRoute(route)\
                   .setActive(route)\
                   .setOrder(index+4)\
                   .setIcon('fa-paper-plane')\
                   .setPermission('post.access')
            if index == 0:
                menu.setHead('Posts')

            menus.append(menu)

        menus.append(
            MenuItem('Category')\
            .setRoute('admin.category.list')\
            .setActive('admin.category.*')\
            .setIcon('fa-folder')\
            .setOrder(index+4)\
            .setPermission('category.access')
        )
        menus.append(
            MenuItem('Tags')\
            .setOrder(index+5)\
            .setRoute('admin.tag.list')\
            .setActive('admin.tag.*')\
            .setIcon('fa-tags')\
            .setPermission('tags.access')
        )

        return menus

    def toolbox(self):
        menus = []
        content_builder = MenuItem('Content Builder').setIcon('fa-magic')
        content_builder.addChild([
            MenuItem('Content Builder')\
            .setRoute('admin.toolbox.type.list')\
            .setIcon('fa-magic')\
            .setPermission('content_type.access')
        ])
        menus.append(content_builder)
        return menus
