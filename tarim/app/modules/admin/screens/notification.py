from app.core.rule import Rule

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.link import Link
from app.modules.admin.core.layout import Layout


class Notification(Screen):

    name = 'Notification'
    description = 'System Notifications'

    permission = 'notification.access'

    @staticmethod
    def rules():
        return [
            Rule('notification', '/notification')
        ]

    def Query(self, **kwargs):
        return {}

    def Layout(self):
        layouts = [
        ]
        return layouts

    """
    After this, coming with metadata
    """

    def breadcrumb(self):
        return 'Notification'
