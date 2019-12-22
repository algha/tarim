from flask import url_for, redirect, request, flash
from app.core.rule import Rule

from flask_login import current_user

from app.modules.admin.core.screen import Screen
from app.modules.admin.core.layout import Layout
from app.modules.admin.core.link import Link
from app.modules.post.models.content_type import ContentType, ContentField
from app.modules.post.models.posts import Post

from ..layouts.post import (PostForm, PostListLayout,
                            PostEditMainLayout, PostEditSideLayout)

class PostList(Screen):

    name = 'Posts'
    description = 'Posts List'

    permission = 'post.access'

    type = ''

    @staticmethod
    def rules():
        return [
            Rule('list', '/<type>/', type = ['native'])
        ]

    def Query(self, type, **kwargs):
        self.content_type = content_type = ContentType.where('slug',type).first()

        PostList.type = type
        self.name = content_type.title
        self.description = content_type.description

        posts = Post.where('type',type).order_by('created_at','desc').get()
        fields = content_type.fields().where('show_in_table', 1).order_by('sort').get()
        return {'posts':posts, 'fields': fields}

    def get_link(self):
        return super().get_link(type=self.type)

    def Layout(self):
        return [
            PostListLayout()
        ]

    def CommandBar(self):
        links = []
        links.append(
            Link('Create',
                 url_for('admin.post.create', type = self.type)
            )
        )
        return links

    def breadcrumb(self):
        return 'Posts'


class PostEdit(Screen):

    name = 'Posts'
    description = 'Posts List'

    permission = 'post.access'

    @staticmethod
    def rules():
        return [
            Rule('create', '/<type>/create', 'POST'),
            Rule('edit', '/<type>/<id>/edit', 'POST')
        ]

    def Query(self, type, id = None, **kwargs):
        content_type = ContentType.where('slug',type).first()
        self.name = content_type.title
        self.description = content_type.description

        self.post = post = Post.first_or_new(id=id).loadRelations()

        return {
            'post': post,
            'fields': content_type.fields().order_by('sort').get()
        }

    def Layout(self):
        layouts = [
            Layout.addLayout('column',[
                PostEditMainLayout,
                PostEditSideLayout
            ])
        ]

        return layouts

    def CommandBar(self):
        links = []
        if hasattr(self.post, 'id'):
            links.append(Link('Delete').setMethod('delete')),
        links.append(Link('Save').setMethod('save'))
        return links

    def delete(self, type, id):
        Post.destroy(id)
        flash('Successfully deleted.', 'success')
        return redirect(url_for('admin.post.list', type=type))

    def save(self, type, id = None, **kwargs):
        post = Post.first_or_new(id=id)

        validationFields = ContentField.where_has('contentType',
            lambda q: q.where('slug', type)
        ).where('regex', '!=', '').order_by('sort').get()

        form = PostForm(validationFields, fomrData = request.form)

        if form.isValidated() == False:
            errors = '<br />'.join(form.getValidationError())
            flash(errors, 'danger')
            return redirect(request.url.replace('/save',''))

        data = form.getFormData()
        data['type'] = type
        post.user_id = current_user.id
        post.fill(data).save()

        if 'category' in data:
            post.categories().sync(data['category'])

        if 'tag' in data:
            post.addTag(data['tag'])

        if 'files' in data:
            post.attachments().sync(data['files'])

        flash('Successfully saved.', 'success')

        return redirect(url_for('admin.post.list', type=type))

    def parents(self):
        return [PostList]

    def breadcrumb(self):
        if hasattr(self.post, 'id'):
            return 'Edit'
        return 'Create'
