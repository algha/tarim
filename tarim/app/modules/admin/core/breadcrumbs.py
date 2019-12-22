class Breadcrumbs:

    def __init__(self, screen):
        self.screens = screen.parents()
        self.current = screen
        self.items = []

    def build(self):
        from app.modules.admin.screens.dashboard import Dashboard
        if not isinstance(self.current, Dashboard):
            self.items.append(BreadcrumbsItem(Dashboard))
        for screen in self.screens:
            self.items.append(BreadcrumbsItem(screen))
        self.items.append(BreadcrumbsItem(self.current, True))
        return self.items

class BreadcrumbsItem:

    def __init__(self, screen, current = False):
        self.screen = screen
        self.current = current

    def getScreen(self):
        if self.current == False:
            return self.screen()
        return self.screen

    def getTitle(self):
        return self.getScreen().breadcrumb()

    def getLink(self):
        if self.current == True:
            return '#'
        return self.getScreen().get_link()

    def isActive(self):
        if self.current == True:
            return 'is-active'
        return ''
