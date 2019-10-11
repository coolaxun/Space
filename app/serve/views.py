from functools import wraps

from flask import g
from flask_restful import Api

from . import serve_blue
from .resources.admin import UserAPI, UserListAPI
from .resources.post import PostAPI, PostListAPI
from ..common.errors import forbidden

api_init = Api(serve_blue)

api_init.add_resource(UserAPI, '/users/<int:user_id>', endpoint='user')
api_init.add_resource(UserListAPI, '/users', endpoint='users')

api_init.add_resource(PostAPI, '/posts/<string:post_id>', endpoint='post')
api_init.add_resource(PostListAPI, '/posts', endpoint='posts')


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)

        return decorated_function

    return decorator
