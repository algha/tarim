
from flask import url_for, redirect, request, jsonify, app
from app.core.rule import Rule
from flask_login import current_user

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.link import Link

from app.modules.admin.blueprint import Toolbox
from app.modules.media.models.attachment import Attachment

from app.core.storage.storage import Storage

class MediaList(Screen):

    name = 'Media'
    description = 'Media List'

    permission = 'media.access'

    @staticmethod
    def rules():
        return [
            Rule('list', type = ['native']),
            Rule('upload', '/upload', 'POST', method = 'Upload'),
            Rule('ajax', '/ajax_media', method = 'ajaxMedia')
        ]

    def Query(self, **kwargs):
        return {'attachments': []}

    def Layout(self):
        layouts = [
        ]
        return layouts

    def CommandBar(self):
        links = [

        ]
        return links

    def ajaxMedia(self, **kwargs):
        name = request.args.get("name")
        return self.render('admin/partials/media.html',name=name, **kwargs)

    def Upload(self):
        files = []
        for file, value in request.files.items():
             data = Storage('local').move(value).getAsDict()
             data['user_id'] = current_user.id

             attachment = Attachment()
             attachment.fill(data).save()

             files.append(attachment.serialize())

        return jsonify({
            'status': 1,
            'message': 'successfully uploaded.',
            'data': files
        })


    def parents(self):
        return []

    def breadcrumb(self):
        return 'Media'
