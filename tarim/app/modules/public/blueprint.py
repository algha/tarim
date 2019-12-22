from flask import render_template, current_app, send_from_directory

from app.core.blueprint import ModuleBlueprint

public = ModuleBlueprint('public',__name__, url_prefix = '/',
                                            template_folder = 'resources/views')

@public.route("")
def home():
    return render_template("home.html")

@public.route("site-map")
def site_map():
    return "<pre>.{0}</pre>".format(current_app.url_map)

@public.route('favicon.ico')
def favicon():
    path = current_app.root_path + '/public/'
    return send_from_directory(path,'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
