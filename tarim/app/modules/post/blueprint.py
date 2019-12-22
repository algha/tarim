from app.core.blueprint import ModuleBlueprint
from .admin.screens.post import PostList, PostEdit
from .admin.screens.category import CategoryList, CategoryEdit
from .admin.screens.tags import TagsList, TagEdit
from .admin.screens.type import TypeList,TypeEdit

from .admin.screens.field import FieldList, FieldEdit

posts = ModuleBlueprint('post',__name__,
                            url_prefix = '/posts',
                            template_folder = 'resources/views')
posts.addScreen(PostList)
posts.addScreen(PostEdit)

category = ModuleBlueprint('category',__name__, url_prefix = '/category')
category.addScreen(CategoryList)
category.addScreen(CategoryEdit)

tag = ModuleBlueprint('tag',__name__, url_prefix = '/tags')
tag.addScreen(TagsList)
tag.addScreen(TagEdit)

type = ModuleBlueprint('type',__name__, url_prefix = '/post/type')
type.addScreen(TypeList)
type.addScreen(TypeEdit)

field = ModuleBlueprint('field',__name__, url_prefix = '/post/field')
field.addScreen(FieldList)
field.addScreen(FieldEdit)
