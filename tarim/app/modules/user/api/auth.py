from flask import current_app
from flask_classful import FlaskView, route
from app import db
from flask import jsonify

#Model
from .. import User
#base api http
from .api import ApiView


class AuthView(ApiView):

    route_base = 'user/auth'

    def index(self):
        return "Auth index"

    def signin(self):
        return "sign view"

    def signup(self):
        my_dict = {"test": 'apple', "a": 'ball'}
        User(name='test',email='email', password='pass', access_token='xx').create()
        return jsonify(my_dict)

    def sendVerifyCode(self):
        pass

    def verifyEmail(self):
        pass

    def forgotpassword(self):
        pass

    def changepassword(self):
        pass
