from flask import current_app
from flask_classful import FlaskView, route
from app import db
from flask import jsonify


#Model
from .. import User
#base api http
from .api import ApiView


class UserView(ApiView):

    route_base = 'user'

    def settings(self):
        return "Settings"
