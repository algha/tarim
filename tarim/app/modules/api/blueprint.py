from app.core.blueprint import ModuleBlueprint

api = ModuleBlueprint('api',__name__, url_prefix = '/api/v1/')

@api.route("info")
def info():
    return "info"
