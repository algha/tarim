from app.core.sys.config import ConfigBase
from flask import send_from_directory, current_app

from .blueprint import blueprint, toolbox
from .core.fields import fields
from .menu import AdminMenus

class Config(ConfigBase):

    key = 'admin'

    @classmethod
    def entryPoint(cls, algha):
        super().entryPoint(algha)
        blueprint.add_blueprint(toolbox)

        algha.asset.setModule('admin').addCSS('/dashboard/assets/css/dashboard.css')
        algha.asset.setModule('admin').addJS('https://use.fontawesome.com/releases/v5.3.1/js/all.js')
        algha.asset.setModule('admin').addJS('/dashboard/assets/js/dashboard.js')

    @classmethod
    def adminMenu(cls):
        return AdminMenus()

    @classmethod
    def blueprints(cls):
        return {
            'admin': blueprint
        }

    @classmethod
    def _blueprints(cls):
        return {
            'admin': blueprint,
            'toolbox': toolbox
        }

    @classmethod
    def fields(cls):
        return fields
