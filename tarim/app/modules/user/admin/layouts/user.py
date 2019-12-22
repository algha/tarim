from flask import url_for

from app.modules.admin.core.layouts import Form, Table, TD
from app.modules.admin.core.fields import (InputField,
                                           SelectField,
                                           PasswordField)
from app.modules.media.admin.core.fields import PictureField

"""
    User form layout
    Add/Edit actions perform here
"""
class UserListLayout(Table):

    data = 'users'

    def filters(self):
        return []

    def fields(self):
        return [
            TD('#').setRender(
                lambda item: self.clousureForID(item)
            ).setWidth(60),
            TD('Name','name'),
            TD('Roles').setRender(
                lambda item:  item.roles.implode('name',', ')
            ),
            TD('Email','email'),
            TD('Created at').setRender(
                lambda item: item.created_at.to_date_string()
            )
        ]

    def clousureForID(self, item):
        return (
            '<a href="{}">{}</a>'\
                .format(url_for('admin.user.edit', id=item.id), item.id)
        )

"""
    User list layout
    List Data here
"""
class UserBaseEditLayout(Form):

    data = 'user'
    name = 'user'

    def fields(self):
        name = (
            InputField('user.name', 'Name')\
            .required()\
            .placeholder('Input your name')
        )

        email = (
            InputField('user.email', 'Email')\
            .placeholder('Input your Email')\
            .set('test')
        )

        account = (
            InputField('user.account', 'Account')\
            .placeholder('Input your Account')
        )

        password = (
            PasswordField('user.password', 'Password')\
            .placeholder('Input your password')
        )

        role = (
            SelectField('user.role', 'Role')\
            .setMultiple()
            .setOptions(self.getChild('roles'))
        )

        return [
            name, email, account, password, role
        ]

    def validation(self):
        return {
            'user.name': 'required',
            'user.email': 'required'
        }

"""
    User list layout
    List Data here
"""
class UserInfoEditLayout(Form):

    data = 'user'
    name = 'user'

    width = 'is-one-third'

    def fields(self):
        locale = (
            SelectField('user.locale', 'Locale')\
            .setOptions({'en': 'English', 'jp': 'Japanese'})
        )

        picture = (
            PictureField('user.picture', 'Picture')\
            .required()
        )

        return [
            locale, picture
        ]
