from flask import render_template, url_for

from .layout import Layout

class Table(Layout):

    template = '/partials/layouts/table.html'

    classList = [
        'is-fullwidth',
        'is-hoverable'
    ]

    sortable_url = None

    def __init__(self):
        super().__init__()

    def build(self, **kwargs):
        return self.render(filters = self.filters(),
                           fields = self.fields(),
                           buttons = self.buttonGroup(),
                           info = self.tableInfo(),
                           attributes = self.loadAttributes(),
                           **kwargs)

    def filters(self):
        return [];

    def fields(self):
        return []

    def buttonGroup(self):
        return []

    def tableInfo(self):
        return ''

    def loadAttributes(self):
        attributes = []
        if self.sortable_url:
            if not '/' in self.sortable_url:
                self.sortable_url = url_for(self.sortable_url)
            attributes.append('data-sortable-url={}'.format(self.sortable_url))
        return ' '.join(attributes)


class TD:
    def __init__(self, title, name = None, render = None):
        self.title = title
        self.name = name
        self.render = render
        self.width = ''
        self.align = 'left'
        self.icon = None
        self.iconfont = None

    def handle(self, data):
        return (self.render)(data)

    def setRender(self, render):
        self.render = render
        return self

    def setWidth(self, width):
        self.width = width
        return self

    def setAlign(self, align):
        self.align = align
        return self

    def setIcon(self, icon, font = 'fas'):
        self.icon = icon
        self.iconfont = font
        return self

    def getValue(self, item):
        if not '.' in self.name:
            return getattr(item, self.name, '')
        names = self.name.split('.')
        value = getattr(item, names[0], '')
        if isinstance(value, dict):
            for name in names[1:]:
                if name in value:
                    value = value[name]
        return value



    def loadModalAsync(self, modal, asyncLoadMethod = None,
                       asyncActionMethod = None, param = None, text = None,
                       textKey = None):
        self.setRender(
            lambda item: self.buildModalAsync(item,
                                              modal,
                                              asyncLoadMethod,
                                              asyncActionMethod,
                                              param,
                                              text,
                                              textKey)
        )
        return self

    def buildModalAsync(self, item, modal, asyncLoadMethod = None,
                        asyncActionMethod = None, param = None,
                        text = None, textKey = None):
        title = ''
        if text is not None:
            title = text
        elif textKey is not None:
            title = getattr(item, textKey) or ''

        param = [getattr(item, param)] or []
        if len(param) > 0:
            key = next(iter(param))
            asyncActionMethod = '/{}/{}'.format(key, asyncActionMethod)


        return render_template('/partials/td/async.html',
                                modal = modal,
                                asyncLoadMethod = asyncLoadMethod or '',
                                asyncActionMethod = asyncActionMethod or '',
                                asyncParams = param,
                                title = title,
                                icon = self.icon,
                                iconfont = self.iconfont)
