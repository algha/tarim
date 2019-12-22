from flask_classful import FlaskView, route
from app.core import ApiView as BaseView

class ApiView(BaseView):

    route_prefix = '/api/v1'

    def index(self):
        return "Api Index"
