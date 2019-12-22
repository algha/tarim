from flask_login import current_user
#$2b$12$vIJXq94Fq809NhiHex7z4e.wmXDhmQeEgAvyYiRAVjb8GkLSI0eLq
class RoleManager(object):

    @classmethod
    def hasPermission(cls, permissions):
        if current_user.is_admin:
            return True
        if permissions is None:
            return True
        if not isinstance(permissions, list):
            permissions = [permissions]

        for role in current_user.roles:
            for permission in permissions:
                return role.actions()\
                           .where('slug', permission)\
                           .count() > 0
        return False
