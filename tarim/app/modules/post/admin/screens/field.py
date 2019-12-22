from flask import url_for, redirect, request, jsonify, flash
from app.core.rule import Rule

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.link import Link
from app.modules.post.models.content_type import ContentType, ContentField

from app.modules.admin.blueprint import Toolbox

from .type import TypeList
from ..layouts.field import FieldListLayout, TypeLinkLayout, FieldEditLayout

class FieldList(Screen):

    name = 'Content Fields'
    description = 'Content Field Builder'

    permission = 'content_type.access'

    @staticmethod
    def rules():
        return [
            Rule('list', '/<id>/type', 'POST'),
            Rule('sort', '/sort', 'POST', method = 'Sort')
        ]

    def Query(self, id, **kwargs):

        types = ContentType.order_by('created_at','desc').get()
        types.each(
            lambda item: setattr(item, 'isActive', item.id == int(id) )
        )
        self.type = type = ContentType.find(id)

        return {
            'types': types,
            'fields': type.fields().order_by('sort').order_by('place').get()
        }

    def Layout(self):
        return [
            Layout.addLayout('column',[
                TypeLinkLayout,
                FieldListLayout
            ]),
            Layout.addLayout('modals',[
                FieldEditLayout
            ]).setModal('getField')
        ]

    def Sort(self):
        items = request.json or []
        for item in items:
            ContentField.find(item['id']).fill({
                'sort': item['sort']
            }).save()
        return jsonify({
            'status': 1,
            'message': 'successfully sorted.'
        })

    def asyncGetField(self, id, **kwargs):
        id = next(iter(request.json), None)
        field = ContentField.first_or_new(id=id)
        return {'field':field}

    def saveField(self, id, param1 = None):
        field = ContentField.first_or_new(id=param1)
        form = FieldEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(url_for('admin.toolbox.field.list',id=id))

        field.fill(form.getFormData())
        ContentType.find(id).fields().save(field)

        flash('Successfully saved.', 'success')

        return redirect(url_for('admin.toolbox.field.list',id=id))

    def CommandBar(self):
        links = []
        links.append(
            Link('Create',
                 url_for('admin.toolbox.field.create',
                 id=self.type.id)
            )
        )
        return []

    def parents(self):
        return [Toolbox, TypeList]

    def breadcrumb(self):
        return 'Content Types'


class FieldEdit(Screen):

    name = 'Content Fields'
    description = 'Content Field Builder'

    permission = 'content_type.view'

    @staticmethod
    def rules():
        return [
            Rule('create','/<id>/type/create','POST'),
            Rule('edit','/<id>/type/<fid>/edit','POST')
        ]

    def Query(self, id, fid = None, **kwargs):
        self.type = ContentType.find(id)
        self.field = ContentField.first_or_new(id=fid)
        return {
            'field': self.field
        }

    def Layout(self):
        return [
            FieldEditLayout()
        ]

    def CommandBar(self):
        links = []
        if hasattr(self.field, 'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return links

    def delete(self, id, fid):
        ContentField.destroy(fid)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.toolbox.field.list', id = id))

    def save(self, id, fid = None):
        field = ContentField.first_or_new(id=fid)
        form = FieldEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        field.fill(form.getFormData())
        ContentType.find(id).fields().save(field)

        flash('Successfully saved.', 'success')

        return redirect(url_for('admin.toolbox.field.list', id = id))

    def parents(self):
        return [Toolbox, TypeList]

    def breadcrumb(self):
        return 'Content Field'
