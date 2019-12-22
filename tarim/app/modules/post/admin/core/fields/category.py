from app.modules.admin.core.fields import SelectField
from app.modules.post.models.category import Category

from app.core.utils.helper import str2arr

class CategoryField(SelectField):

    type = 'category'
    title = 'Category'

    def __init__(self, name = None, label = None, post_type = None, **kwargs):
        super().__init__(name, label, **kwargs)

        self.options = Category.where('type',post_type)\
                                .order_by('sort').get().pluck('title', 'id')

    def initAttributes(self):
        self.attributes = {
            'name': 'category',
            'multiple': True
        }
