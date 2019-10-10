from functools import wraps

from flask import request, g
from flask_restful import Resource, Api

from app.serve import serve_blue
from app.serve.models import Post
from app.models import User
from app.common.errors import forbidden

api_init = Api(serve_blue)


class UserAPI(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            data = {'id': user_id, 'name': user.username}
        else:
            data = {'id': '', 'name': ''}
        return data

    def post(self, user_id):
        pass

    def put(self, user_id):
        pass


class UserListAPI(Resource):
    # method_decorators = [auth.login_required]

    def get(self):
        users = User.query.all()
        return {'users:': users[0].id}


api_init.add_resource(UserAPI, '/users/<int:user_id>', endpoint='user')
api_init.add_resource(UserListAPI, '/users', endpoint='users')


class PostAPI(Resource):
    def get(self, post_id):
        post = Post.objects.filter(id=post_id)
        if not post:
            data = dict(msg='not found')
        else:
            data = dict(id=post.id, name=post.title)
        return data

    def put(self, post_id):
        data = request.json
        post = Post.objects.filter(id=post_id)
        result = dict(msg='not found')
        if post:
            Post.objects.filter(id=post_id).update(**data)
        result['msg'] = 'ok'
        return result


class PostListAPI(Resource):

    def get(self):
        pass

    def post(self):
        pass


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)

        return decorated_function

    return decorator


# api_init.handle_error