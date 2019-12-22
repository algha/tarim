from app.core.rule import Rule

from app.core.template import BaseTemplate
from app.modules.admin.core.screen import Screen
from app.modules.admin.core.link import Link
from app.modules.admin.core.layout import Layout

class ToolboxTemplate(BaseTemplate):
    template = 'toolbox.html'

class Toolbox(Screen):

    template = ToolboxTemplate

    name = 'Toolbox'
    description = 'Toolbox'

    permission = 'toolbox.access'

    @staticmethod
    def rules():
        return [
            Rule('list')
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
        return 'Toolbox'
