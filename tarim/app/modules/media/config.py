from app.core.sys.config import ConfigBase

from .blueprint import admin, media

from .admin.core.fields import fields

from .models.attachment import Attachment

from .menu import AdminMenus

class Config(ConfigBase):

    key = 'media'

    @classmethod
    def entryPoint(cls, algha):
        super().entryPoint(algha)

        _admin = algha.getBlueprint('admin', 'admin')
        _admin.add_blueprint(admin)

        algha.asset.setModule('admin').addJS('/media/assets/js/admin.js')
        algha.asset.setModule('admin').addCSS('/media/assets/css/admin.css')

    @classmethod
    def adminMenu(cls):
        return AdminMenus()

    @classmethod
    def blueprints(cls):
        return {
            'media': media
        }

    @classmethod
    def _models(cls):
        return {
            'attachment': Attachment
        }

    @classmethod
    def fields(cls):
        return fields
