from app.core.sys.config import ConfigBase

from .blueprint import api


class Config(ConfigBase):

    key = 'api'

    @classmethod
    def entryPoint(cls, algha):
        super().entryPoint(algha)


    @classmethod
    def blueprints(cls):
        return {
            'api': api
        }
