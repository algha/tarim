from orator.orm import has_many, belongs_to_many
from app.core.model import Model



class Category(Model):

    __table__ = 'category'

    __fillable__ = [
        'title',
        'type',
        'slug',
        'options',
        'description'
    ]

    __casts__ = {
        'options': 'dict'
    }

    @belongs_to_many('category_posts')
    def posts(self):
        from .posts import Post
        return Post
