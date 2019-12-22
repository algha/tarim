from flask import url_for, redirect
from flask_login import logout_user
from app.core.rule import Rule

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.link import Link
from app.modules.admin.core.layout import Layout

class Dashboard(Screen):

    name = 'Dashboard'
    description = 'Welcome to dashboard panel'

    permission = 'dashboard.access'

    @staticmethod
    def rules():
        return [
            Rule('main', '/main'),
            Rule('logout', '/logout', method = 'Logout')
        ]

    def Query(self, **kwargs):
        return {}

    def Layout(self):
        return []

    def CommandBar(self):
        children = [Link('Logout', url_for('admin.logout'))]
        links = [
            Link('Add New', '#'),
            Link.withChildren('User',children)
        ]
        return  links

    def Logout(self):
        logout_user()
        return redirect(url_for('admin.main'))

    """
    After this, coming with metadata
    """
    def breadcrumb(self):
        return 'Dashboard'
