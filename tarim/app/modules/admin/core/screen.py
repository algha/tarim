from flask import url_for, request
from flask_login import current_user, login_required
from app import algha, login

from app.core.view import BaseView
from app.core.template import BaseTemplate
from app.modules.admin.core.menu import Menu, MenuItem
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.breadcrumbs import Breadcrumbs
from app.modules.user.models.user import User

from .repository import Repository


from app.modules.admin.core.permission import ScreenPermission

@login.user_loader
def user_loader(id):
    return User.find(id)

class ScreenTemplate(BaseTemplate):
    template = 'main.html'

class Screen(BaseView):

    template = ScreenTemplate

    name = ''
    description = ''

    permission = None

    @staticmethod
    def rules():
        return []

    def __eq__(self, other):
        return self.name == other.name

    def get_link(self, **options):
        name = self.rules()[0].name
        return url_for('{}.{}'.format(self.blueprint.name, name), **options)

    def Query(self, **kwargs):
        raise NotImplementedError()

    def Layout(self):
        return []

    def buildView(self):
        layout = Layout.addLayout('blank',self.Layout())
        return layout.build(self.query)

    def CommandBar(self):
        return []

    @login_required
    @ScreenPermission()
    def get(self, *args, **kwargs):
        for rule in self.rules():
            if rule.hasSecondary() and rule.isRule(request.endpoint):
                return getattr(self, rule.method)(**kwargs)

        if 'method' in kwargs:
            return self.buildMethod(**kwargs)

        self.query = Repository(self.Query(**kwargs))

        return self.getTemplate(
            screen = self,
            breadcrumbs = Breadcrumbs(self).build(),
            Menu = self.getMenus(),
            title = self.name,
            description = self.description
        )

    def buildMethod(self, **kwargs):
        method = kwargs.get('method')
        del kwargs['method']
        if '/' in method:
            methods = method.split('/')
            method = methods.pop()
            for i in range(len(methods)):
                key = "param{}".format(i+1)
                kwargs[key] = methods[i]

        if hasattr(self, method) == False:
            return ('not found the method {}'.format(method))
        if method.startswith('async'):
            return self.handleAsync(method = method, **kwargs)
        return getattr(self, method)(**kwargs)


    def handleAsync(self, method, param1, **kwargs):
        query = getattr(self, method)(**kwargs)
        query = Repository(query)
        for layout in self.Layout():
            if hasattr(layout, 'templateSlug') and layout.templateSlug == param1:
                return layout.build(query, True)
        return 'not handled'

    """ Breadcrumbs data """
    def parents(self):
        return []

    def breadcrumb(self):
        return ''

    """ Helper methods """
    def getMenus(self):
        menus = []
        toolboxes = []

        for config in algha.getConfigs():
            adminMenu = config.adminMenu()
            if adminMenu is None:
                continue
            menus.extend(adminMenu.menu())
            toolboxes.extend(adminMenu.toolbox())

        menu = Menu()
        menu.addMenuItem('menu',menus)
        menu.addMenuItem('toolbox',toolboxes)
        return menu
