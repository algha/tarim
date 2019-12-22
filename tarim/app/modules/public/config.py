from app import algha

from app.core.sys.config import ConfigBase

from .blueprint import public


class Config(ConfigBase):

    key = 'public'

    @classmethod
    def entryPoint(cls, algha):
        super().entryPoint(algha)


    @classmethod
    def blueprints(cls):
        return {
            'public': public
        }
