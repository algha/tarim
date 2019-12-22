from .layout import Layout

class Link(Layout):

    template = None

    background = 'has-background-light'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.classList.append(self.background)

    def build(self, **kwargs):
        return self.render(name = self.name,
                           items = self.items(),
                           **kwargs)

    def items(self):
        return []


class VerticalLink(Link):
    template = '/partials/layouts/vlink.html'



class HorizontalLink(Link):
    template = '/partials/layouts/hlink.html'


class LinkItem():
    def __init__(self, title, link, active = False):
        self.title = title
        self.link = link
        self.active = active
        self.info = None
        self.badge = None

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link

    def setInfo(self, info):
        self.info = info
        return self

    def getBadge(self):
        return self.badge

    def setBadge(self, badge):
        self.badge = badge
        return self

    def getInfo(self):
        return self.info

    def getActive(self):
        return self.active

    def isActive(self):
        if self.getActive():
            return 'is-active'
        return ''
