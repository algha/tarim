import os

dbconfig = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'db',
        'database': 'tarim',
        'user': 'Tarim',
        'password': 'Tarim123',
        'prefix': ''
    }
}

modules = [
    'app.modules.admin',
    'app.modules.public',
    'app.modules.api',
    'app.modules.post',
    'app.modules.media',
    'app.modules.user',
]


class Config:
    SECRET_KEY = "?\x0b\x8a\xf9C\x91\xd3\xd2\xe7U\x01\xe1\x0f\xda\x99^YB\xd8\xe1\xb6\x83\xa8i"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ORATOR_DATABASES = dbconfig
    ALGHA_MODULES = modules
    ADMIN_PREFIX = '/dashboard'
    #MAIL_SERVER = 'smtp.googlemail.com'
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('EMAIL_USER')
    #MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
