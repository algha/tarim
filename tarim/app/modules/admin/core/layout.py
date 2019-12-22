from hashlib import md5
from flask import render_template

class Layout:

    templates = [
        'tab',
        'column', # can settings column size
        'modal',
        'blank'
    ]

    template = 'blank'
    #
    # def __repr__(self):
    #     return 'template: {}'.format(self.template)

    def __init__(self, template, layout, name = None):
        self.layouts = layout
        self.template = template
        self.asyncButtons = []
        self.modal = None
        self.modalLayouts = []
        self.templateSlug = None

    @classmethod
    def addLayout(cls, template, layout):
        if not isinstance(layout, list):
            layout = [layout]
        return cls(template, layout)

    def render(self, layouts, **kwargs):
        return render_template('layouts/{}.html'.format(self.template),
                               forms = layouts,
                               asyncButtons = self.asyncButtons,
                               modal = self.modal,
                               templateSlug = self.templateSlug,
                               layout = self)

    def addAsyncButton(self, button):
        self.asyncButtons.append(button)
        return self

    def setModal(self, modal):
        self.modal = modal
        self.templateSlug = md5(modal.encode('utf-8')).hexdigest()
        return self

    def build(self, query, asyncLoad = False):
        if asyncLoad:
            self.template = 'blank'
        layouts = self.buildView(query, self.layouts)
        return self.render(layouts)

    def buildView(self, query, layouts):
        _layouts = []

        for layout in layouts:
            if isinstance(layout, Layout):
                if layout.template == 'modals':
                    self.modalLayouts.append(layout)
                _layouts.append(layout.build(query))
                continue
            if callable(layout):
                layout = layout()
            layout.setRepository(query)
            _layouts.append(layout)

        return _layouts

    def getModals(self):
        return self.modalLayouts

    def filter(self, name):
        _layout = None
        for layout in self.layouts:
            if isinstance(layout, Layout):
                _layout = layout.filter(name)
                continue
            if layout.name == name:
                _layout = layout
                break
        return _layout


    def buildOrPrint(self, data):
        if isinstance(data, str):
            return data
        else:
            return data.build()
