from flask import redirect, url_for
from flask_login import current_user
from .role_manager import RoleManager

class Permission(object):

    def __init__(self,permission = None, prefix = None):
        if not isinstance(permission, list):
            permission = [permission]
        self.permission = permission


class ScreenPermission(Permission):
    def __call__(self, original_func):
        def wrappee( *args, **kwargs):
            screen = args[0]
            if not RoleManager.hasPermission(screen.permission):
                return redirect(url_for('admin.login'))
            fn = original_func(*args,**kwargs)
            return fn
        return wrappee

class MethodPermission(Permission):
    def __call__(self, original_func):
        permissions = self.permission
        def wrappee( *args, **kwargs):
            if not RoleManager.hasPermission(permissions):
                return redirect(url_for('admin.login'))
            fn = original_func(*args,**kwargs)
            return fn
        return wrappee
