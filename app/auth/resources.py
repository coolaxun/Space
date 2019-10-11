from flask_restful import Resource, marshal_with

from .. import db
from ..models.admin import User
from ..common.parsers import signin_parser, signup_parser
from ..common.fields import signin_fields, signup_fields


class SignIn(Resource):

    @marshal_with(signin_fields)
    def post(self):
        signin_args = signin_parser.parse_args()
        user = User.query.filter_by(username=signin_args.username).first()
        if not user:
            return {'message': 'user does not existed'}
        elif not user.verify_password(signin_args.password):
            return {'message': 'password error'}
        token = user.generate_auth_token(3600)
        return {'token': token.decode('ascii'), 'code': 20000, 'success': 1}


class SignOut(Resource):

    def get(self):
        return {'success': 1}


class SignUp(Resource):

    @marshal_with(signup_fields)
    def post(self):
        sign_up_args = signup_parser.parse_args()
        username = sign_up_args.username
        password = sign_up_args.password
        user = User.query.filter_by(username=username).first()
        if user:
            return {'message': 'user has existed'}
        new_user = User()
        new_user.username = username
        new_user.password = password
        db.session.add(new_user)
        db.session.commit()
        return {'success': 1, 'message': '注册成功'}
