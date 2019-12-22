from app.config import Config
from flask import send_from_directory, current_app
from app.core.blueprint import ModuleBlueprint
from .screens.dashboard import Dashboard
from .screens.notification import Notification
from .screens.toolbox import Toolbox
from .view import LoginView

blueprint = ModuleBlueprint('admin', __name__, url_prefix = Config.ADMIN_PREFIX,
                            template_folder = 'resources/views/')

blueprint.addView(LoginView)
@blueprint.route('/assets/<path:filename>')
def assets(filename):
    path = current_app.root_path + '/modules/admin/public/'
    return send_from_directory(path,filename);

blueprint.addScreen(Notification)
blueprint.addScreen(Dashboard)

toolbox = ModuleBlueprint('toolbox', __name__, url_prefix = '/toolbox')
toolbox.addScreen(Toolbox)
