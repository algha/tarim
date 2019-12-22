from app.core.sys.config import ConfigBase

from .blueprint import posts, category, tag, type, field
from .admin.core.field import FieldsList
from .admin.core.fields import fields

from .models.category import Category
from .models.posts import Post
from .models.tags import Tags

from .menu import AdminMenus

class Config(ConfigBase):

    key = 'post'

    @classmethod
    def entryPoint(cls, algha):
        admin = algha.getBlueprint('admin', 'admin')
        admin.add_blueprint(posts)
        admin.add_blueprint(category)
        admin.add_blueprint(tag)

        toolbox = algha.getBlueprint('admin', 'toolbox')
        toolbox.add_blueprint(type)
        toolbox.add_blueprint(field)

    @classmethod
    def adminMenu(cls):
        return AdminMenus()

    @classmethod
    def postRelations(cls):
        return [
            'category',
            'tag'
        ]

    @classmethod
    def _models(cls):
        return {
            'category': Category,
            'post': Post,
            'tags': Tags
        }

    @classmethod
    def field_types(cls):
        return FieldsList().as_dict()

    @classmethod
    def fields(cls):
        return fields
