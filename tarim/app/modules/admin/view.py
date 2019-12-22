from flask import request, redirect, url_for
from flask_login import login_user
from app.core.view import BaseView
from app.core.template import BaseTemplate
from app.modules.user.models.user import User

class LoginTemplate(BaseTemplate):

    template = 'signin.html'

class LoginView(BaseView):

    rule = '/login'

    name = 'login'

    methods = ['GET', 'POST']

    template = LoginTemplate

    def get(self):
        error = None
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = User.where('email', email).first()
            if not user:
                error = 'This user is not exist.'
            elif not user.check_password(password):
                error = 'Password is not correct.'
            else:
                login_user(user)
                return redirect(url_for('admin.main'))

        return self.getTemplate(error = error)

    def title(self):
        return 'Login'

    def description(self):
        return 'Login Page'
