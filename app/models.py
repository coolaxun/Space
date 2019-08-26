from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import login_manager
from datetime import datetime
from flask import current_app

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    roles = db.relationship('Role', backref='user', lazy='dynamic')
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # posts = db.relationship('POST', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    # users = db.relationship('User', backref='role', lazy='dynamic')


# class UserProfile(db.Model):
#     __tablename__ = 'user_profiles'
#


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    create_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_json(self):
        json_post = {
            'body': self.body
        }
        return json_post


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Permission:
    FOLLOW = 0x01

