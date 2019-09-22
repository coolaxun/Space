from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

from app import db
from app import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)
    phone = db.Column(db.String(64), unique=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # roles = db.relationship('Role', secondary=user_roles, backref='users', lazy='dynamic')

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')

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


# relationship table
# the relation between Role and Permission is many-to-many
permission_role = db.Table('permission_role',
                           db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                           db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'))
                           )

# relationship table
# the relation between Permission and Resource is many-to-many
permission_resource = db.Table('permission_resource',
                               db.Column('permission_id', db.Integer, db.ForeignKey('permission.id')),
                               db.Column('resource_id', db.Integer, db.ForeignKey('resource.id'))
                               )


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    enabled = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    default = db.Column(db.Boolean, default=False)
    # users = db.relationship('User', backref='roles', lazy='dynamic')
    perms = db.relationship('Permission', secondary=permission_role, backref=db.backref('roles', lazy='dynamic'))


class Permission(db.Model):
    __tablename__ = 'permission'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(64))
    enabled = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    resources = db.relationship('Resource', secondary=permission_resource, backref=db.backref('perms', lazy='dynamic'))


class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(64))
    route = db.Column(db.String(64))
    parent_id = db.Column(db.Integer)
    func = db.Column(db.String(64))
    category = db.Column(db.String(10))
    enabled = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)


# class Menu(db.Model):
#     __tablename__ = 'menu'
#     id = db.Column(db.Integer, primary_key=True)
#     alias = db.Column(db.String(10), unique=True)
#     name = db.Column(db.String(64))
#     parent_id = db.Column(db.Integer)
#     visible = db.Column(db.Boolean, default=True)
#     enabled = db.Column(db.Boolean, default=True)
#     create_time = db.Column(db.DateTime, default=datetime.utcnow)


# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer, primary_key=True)
#     # title = db.Column(db.String(128), nullable=False)
#     title = db.Column(db.String(128))
#     body = db.Column(db.Text)
#     create_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     def to_json(self):
#         json_post = {
#             'body': self.body
#         }
#         return json_post


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class Permission:
#     FOLLOW = 0x01
