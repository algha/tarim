from flask import url_for, redirect, flash, request, jsonify
from app.core.rule import Rule

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.link import Link

from app.modules.post.models.tags import Tags, Taggable

from ..layouts.tags import (TagsListLayout, TagEditLayout)

class TagsList(Screen):

    name = 'Tags'
    description = 'Tags List'

    permission = 'tags.access'

    @staticmethod
    def rules():
        return [
            Rule('list', '', type = ['native']),
            Rule('search', '/search', method = 'Search')
        ]

    def Query(self, **kwargs):
        tags = Tags.get()
        return {'tags': tags}

    def Layout(self):
        layouts = [
            TagsListLayout
        ]
        return layouts

    def CommandBar(self):
        links = [

        ]
        return links

    def Search(self):
        key = request.args.get('search') or ''
        tags = Tags.where('name','like', '%{}%'.format(key)).get()
        tags.each(lambda item: setattr(item, 'text', item.name))

        return jsonify({
            'status': 1,
            'message': 'successfully sorted.',
            'data': tags.serialize()
        })

    def breadcrumb(self):
        return 'Tags'


class TagEdit(Screen):

    name = 'Tag'
    description = 'Tag Edit'

    permission = 'tags.access'

    @staticmethod
    def rules():
        return [
            Rule('edit', '/<id>/edit', 'POST')
        ]

    def Query(self, id = None, **kwargs):
        self.tag = tag = Tags.first_or_new(id=id)
        return {'tag':tag}

    def Layout(self):
        return [TagEditLayout()]

    def CommandBar(self):
        links = []
        links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return links

    def delete(self, id):
        Taggable.where('tag_id', id).delete()
        Tags.destroy(id)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.tag.list'))

    def save(self, id = None, **kwargs):
        tag = Tags.first_or_new(id=id)
        form = TagEditLayout(request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        tag.fill(form.getFormData()).save()
        flash('Successfully saved.', 'success')
        return redirect(url_for('admin.tag.list'))

    def parents(self):
        return [TagsList]

    def breadcrumb(self):
        return 'Edit'
