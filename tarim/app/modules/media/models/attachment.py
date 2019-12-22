from orator.orm import has_many, belongs_to_many, accessor
from app.core.model import Model
from flask import request


class Attachment(Model):

    __table__ = 'attachments'

    __fillable__ = [
        'user_id',
        'name',
        'original_name',
        'mime',
        'extension',
        'size',
        'path',
        'description',
        'alt',
        'hash',
        'disk',
        'group'
    ]

    __appends__ = [
        'url',
        'file_type'
    ]

    __images__ = [
        'png',
        'jpg',
        'jpeg'
    ]

    __video__ = [
        'mp4'
    ]

    __pdf__ = [
        'pdf'
    ]


    def getFolder(self):
        url = self.path
        url += self.name
        url += ".{0}".format(self.extension)
        return url

    @accessor
    def url(self):
        url = ''
        if self.disk == 'local':
            url = request.url_root+"media/"
        url += self.getFolder()
        return url

    @accessor
    def file_type(self):
        if self.extension in self.__images__:
            return 'photo'

        if self.extension in self.__video__:
            return 'video'

        if self.extension in self.__pdf__:
            return 'pdf'

        return 'file'




class Attachmentable(Model):

    __table__ = 'attachmentable'

    __timestamps__ = False
