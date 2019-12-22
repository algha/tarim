from orator.orm import has_many, belongs_to
from app.core.model import Model

class ContentType(Model):

    __table__ = 'content_type'

    __fillable__ = [
        'title',
        'slug',
        'description'
    ]

    @has_many
    def fields(self):
        return ContentField

class ContentField(Model):

    __table__ = 'content_field'

    __fillable__ = [
        'field_type',
        'title',
        'name',
        'sort',
        'is_required',
        'regex',
        'place',
        'show_in_table',
        'dataattr'
    ]

    @belongs_to
    def contentType(self):
        return ContentType
