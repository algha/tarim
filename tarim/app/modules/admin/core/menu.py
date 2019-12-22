from flask import url_for, render_template
from app.core.utils.route import in_route

from .role_manager import RoleManager

class Menu:

    def __init__(self):
        self.place = {}

    def addMenuItem(self, place, item):
        if not isinstance(item, list):
            item = [item]
        self.addItemsToPlace(place, item)
        return self

    def addItemsToPlace(self, place, items):
        if not place in self.place:
            self.place[place] = items
        else:
            self.place[place] = self.place[place].extend(items)

    def getItemsInPlace(self, place):
        if not place in self.place:
            return []
        return self.place[place]

    def getAllMenus(self):
        allMenus = []
        allPlaces = []
        for place, menus in self.place.items():
            allMenus = allMenus + menus
            allPlaces.append(place)
        return (allPlaces, allMenus)


class MenuItem:

    template = 'sidebar/menu.html'

    def __init__(self, title,
                order = 0, route = None,
                divider = False, head = None):
        self.title = title
        self.order = order
        self.route  = route
        self.diverder = divider
        self.head = head
        self.permission = None
        self.children = []
        self.parent = None
        self.active = None

    def render(self, **kwargs):
        return render_template(self.template,
                               **kwargs)

    def build(self, **kwargs):
        if not RoleManager.hasPermission(self.permission):
            return ''
        return self.render(menu = self,
                           **kwargs)

    def addChild(self, menu):
        self.children.extend(menu)
        return self

    def appendChild(self, menu):
        self.children.append(menu)
        return self

    def setPermission(self, permission):
        self.permission = permission
        return self

    def setTitle(self, title):
        self.title = title
        return self

    def setOrder(self, order):
        self.order = order
        return self

    def setRoute(self, route):
        self.route = route
        return self

    def setDivider(self, diverder):
        self.diverder = diverder
        return self

    def setHead(self, head):
        self.head = head
        return self

    def setDivier(self, divider):
        self.diverder = divider
        return self

    def setParent(self, parent):
        self.parent = parent
        return self

    def setIcon(self, icon, font = 'fas'):
        self.icon = icon
        self.iconfont = font
        return self

    def setActive(self, route):
        self.active = route
        return self

    def url(self):
        if self.route is None:
            return 'javascript:;'
        if '/' in self.route:
            return self.route
        return url_for(self.route)

    def dataAction(self):
        if len(self.children) > 0:
            return 'data-action="click->layouts--menu#toggleMenu"'
        return ''

    def linkClass(self):
        _class = []
        if in_route(self.getActivies(self)):
            _class.append('is-active')
        if len(self.children) > 0:
            _class.append('is-toggle')
        if self.parent is not None:
            _class.append('has-padding-l-3')
        return ' '.join(_class)

    def liClass(self):
        _class = []

        if len(self.children) > 0:
            _class.append('has-children')

        is_in_route = in_route(self.getActivies(self))
        if is_in_route and self.parent is None:
            _class.append('is-active')
        return ' '.join(_class)

    def getActivies(self, menu):
        activies = [menu.active]
        for _menu in menu.children:
            activies.extend(_menu.getActivies(_menu))
        return activies
        # return self.active

    def hasChildren(self):
        return len(self.children) > 0

class AdminMenu:

    def menu(self):
        return []

    def toolbox(self):
        return []
