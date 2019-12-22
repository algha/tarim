from flask import url_for
from flask import render_template

class LinkBase():

    template = None
    name = ''

    def render(self, **kwargs):
        return render_template(self.template,
                               link = self,
                               **kwargs)

class Link(LinkBase):

    template = '/partials/layouts/link.html'

    def __init__(self, title, link = None, children = None):
        self.title = title
        self.link = link

        if children is not None:
            self.children = children
        else:
            self.children = []

        self.method = None

        self.modal = None
        self.asyncLoadMethod = None,
        self.asyncActionMethod = None,
        self.asyncParams = None

        self.iconfont = 'fas'
        self.icon = None

        self.hoverable = False
        self.divider = False

        self.confirm = ''

        self.ajaxMethod = None

        self.parent = None

        self._class = []

    def build(self, **kwargs):
        return self.render()

    def setTitle(self, title):
        self.title = title
        return self

    def setMethod(self, method):
        self.method = method
        return self

    def loadModalAsync(self,
                       modal,
                       asyncLoadMethod = None,
                       asyncActionMethod = None,
                       asyncParams = None):
        self.modal = modal
        self.asyncLoadMethod = asyncLoadMethod or ''
        self.asyncActionMethod = asyncActionMethod or ''
        self.asyncParams = asyncParams or []
        return self

    def getAsyncActionMethod(self, request):
        if self.asyncActionMethod:
            params = ''
            if len(self.asyncParams) > 0:
                params = '/'.join(str(v) for v in self.asyncParams)
                params = params+'/'
            method = "{}/{}{}".format(
                request.url,
                params,
                self.asyncActionMethod
            )
            return method
        return ''

    def setLink(self, link):
        self.link = link
        return self

    def setDivider(self, divider):
        self.divider = divider
        return self

    def setConfirm(self, confirm):
        self.confirm = confirm
        return self

    def setIcon(self, icon, font = 'fas'):
        self.icon = icon
        self.iconfont = font
        return self

    def setAjaxMethod(self, method):
        self.ajaxMethod = method
        return self

    def getHoverable(self):
        if self.hoverable:
            return 'is-hoverable'
        return ''

    def getClass(self):
        if self.parent:
            self._class.append('dropdown-item')
        if self.parent is None:
            self._class.append('button')
        return ' '.join(self._class)

    def appendChild(self, child):
        self.setIcon('fa-angle-down')
        child.parent = self
        self.children.append(child)
        return self

    def appendChildren(self, children):
        self.setIcon('fa-angle-down')
        _children = []
        for child in children:
            child.parent = self
            _children.append(child)
        self.children.extend(_children)
        return self

    @classmethod
    def withChildren(cls, title, children):
        _children = []
        for child in children:
            child.parent = cls
            _children.append(child)
        return cls(title, children = _children)
