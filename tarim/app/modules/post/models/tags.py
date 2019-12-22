from orator.orm import has_many, belongs_to_many
from app.core.model import Model

class Tags(Model):

    __table__ = 'tags'

    __timestamps__ = False

    __fillable__ = [
        'name',
        'count',
        'slug',
        'type'
    ]

    @belongs_to_many('taggable')
    def posts(self):
        from .posts import Post
        return Post

class Taggable(Model):

    __table__ = 'taggable'

    __timestamps__ = False
