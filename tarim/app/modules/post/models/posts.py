from orator.orm import has_many, belongs_to_many, belongs_to

from app import algha

from app.core.model import Model
from .content_type import ContentType

from slugify import slugify

class TagHelper:

    def addTag(self, tags):
        if not isinstance(tags, list):
            tags = [tags]

        tagsId = []

        for _tag in tags:
            tag = self.tagModel().first_or_create(
                slug = _tag #slugify(_tag)
            )
            tag.fill({
                'name': _tag,
                'count': getattr(tag, 'count', 0) + 1
            }).save()

            tagsId.append(tag.id)

        self.tags().sync(tagsId)
        return True


    def removeTag(self, tags):
        if not isinstance(tags, list):
            tags = [tags]
        for tag in tags:
            tag = slugify(tag)

class Post(Model, TagHelper):

    __table__ = 'posts'

    __fillable__ = [
        'type',
        'content'
    ]

    __casts__ = {
        'content': 'dict'
    }

    __relation__ = [
        'category',
        'tag'
    ]

    def tagModel(self):
        return algha.getModel('post', 'tags')

    @belongs_to
    def user(self):
        return algha.getModel('user', 'user')

    def getContent(self, key):
        if key in self.content:
            return self.content[key]
        return ''

    def setContent(self, key, content):
        self.content[key] = content
        return self

    @belongs_to_many('category_posts')
    def categories(self):
        return algha.getModel('post', 'category')

    @belongs_to_many('attachmentable', 'attachmentable_id')
    def attachments(self):
        return algha.getModel('media', 'attachment')

    @belongs_to_many('taggable')
    def tags(self):
        return self.tagModel()

    def postType(self):
        return ContentType.where('slug',self.type).first()

    def isRelatedWith(self, key):
        return self.postType()\
                   .fields.filter(
                        lambda item: item.field_type == key
                    ).count() > 0

    def loadRelations(self):
        if not hasattr(self, 'id'):
            return self

        if self.isRelatedWith('category'):
            categories = self.categories.pluck('id').map(lambda id: str(id))
            self.setAttribute('category', categories.serialize())

        if self.isRelatedWith('tag'):
            self.setAttribute('tag', self.tags.pluck('name').serialize())

        if self.isRelatedWith('upload'):
            self.setAttribute('files', self.attachments)

        return self
