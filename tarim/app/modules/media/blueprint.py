from flask import send_from_directory, current_app

from app.core.blueprint import ModuleBlueprint

from .admin.screens.media import MediaList

admin = ModuleBlueprint('media',__name__,
                               url_prefix = '/media',
                               template_folder = 'resources/views')
admin.addScreen(MediaList)


media = ModuleBlueprint('media',__name__,
                               url_prefix = '/media',
                               template_folder = 'resources/views')
@media.route('/storage/<path:filename>')
def files(filename):
    try:
        return send_from_directory(current_app.root_path + '/storage/',
                                   filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@media.route('/assets/<path:filename>')
def assets(filename):
    path = current_app.root_path + '/modules/media/public/'
    return send_from_directory(path,filename);
