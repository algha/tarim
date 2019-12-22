from flask_login import UserMixin
from app import bcrypt
from orator.orm import belongs_to_many
from app.core.model import Model

from .role import Role


class User(Model, UserMixin):

    __table__ = 'users'

    __fillable__ = [
        'name',
        'email',
        'account',
        'password',
        'status',
        'picture'
    ]

    __hidden__ = ['password']

    @belongs_to_many('user_role')
    def roles(self):
        return Role

    def set_password(self, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        if not self.password or not password:
            return False
        return bcrypt.check_password_hash(self.password, password)

# class Profile(Model):
#
#     __tablename__ = 'user_profile'
#
#     id = db.Column(db.Integer, primary_key=True)
#
#     # basic information
#     avatar = db.Column(db.String(200))
#     gender = db.Column(db.String(10))
#     status = db.Column(db.String(500))
#     is_online = db.Column(db.Integer, default=0)
#     be_notified = db.Column(db.Integer, default=1)
#
#     # dates of the user activity
#     last_seen_at = db.Column(db.DateTime)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow)
#     deleted_at = db.Column(db.DateTime)
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#
# class Device(Model):
#
#     __tablename__ = 'user_device'
#
#     id = db.Column(db.Integer, primary_key=True)
#
#     # basic information
#     os = db.Column(db.String(60), nullable=False)
#     model = db.Column(db.String(60), nullable=False)
#     version = db.Column(db.String(60), nullable=False)
#     token = db.Column(db.String(200), nullable=False)
#
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     deleted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#
#
# class Verification(Model):
#
#     __tablename__ = 'user_verification'
#
#     id = db.Column(db.Integer, primary_key=True)
#     verify_token = db.Column(db.String(60), nullable=False)
#     expire_at = db.Column(db.DateTime, nullable=False,)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     deleted_at = db.Column(db.DateTime)
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#
# class PasswordReset(Model):
#
#     __tablename__ = 'password_resets'
#
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.Integer, db.ForeignKey('user.email'), nullable=False)
#     token = db.Column(db.String(60), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     expire_at = db.Column(db.DateTime, nullable=False)
#
# class AuthHistory(Model):
#
#     __tablename__ = 'auth_history'
#
#     id = db.Column(db.Integer, primary_key=True)
#     os = db.Column(db.String(100), nullable=False)
#     platform = db.Column(db.String(100), nullable=False)
#     platform_version = db.Column(db.String(100), nullable=False)
#     browser = db.Column(db.String(100), nullable=False)
#     browser_version = db.Column(db.String(100), nullable=False)
#     ip_address = db.Column(db.String(100), nullable=False)
#
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
