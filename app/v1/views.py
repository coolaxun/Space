from functools import wraps

from flask import jsonify, g
from flask_restful import Resource, Api

from app.v1 import api
from app.models import User
from app.v1.errors import forbidden

api_init = Api(api)


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


@api.errorhandler(404)
def page_not_found(e):
    response = jsonify({'error': 'not found'})
    response.status_code = 404
    return response


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator



