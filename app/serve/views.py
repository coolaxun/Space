from functools import wraps

from flask import jsonify, g
from flask_restful import Resource, Api

from app.serve import serve_blue
from app.models import User
from app.common.errors import forbidden

api_init = Api(serve_blue)


class UserAPI(Resource):
    def get(self, user_id):
        return User.query.filter_by(id=user_id).first().id

    def post(self, id):
        pass


class UserListAPI(Resource):
    # method_decorators = [auth.login_required]

    def get(self):
        users = User.query.all()
        print(users[0].id)
        return {'users:': users[0].id}


api_init.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
api_init.add_resource(UserListAPI, '/users', endpoint='users')


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator



