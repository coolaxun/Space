from flask_restful import Resource, Api

from app.serve.models import Post
from app.public import public

public_api = Api(public)


class UserInfoAPI(Resource):

    def get(self, user_id):
        post = Post.objects.all().first()
        # user = User.query.filter_by(id=user_id).first()
        if post:
            data = dict(id=str(post.id), name=post.title)
        else:
            data = dict(id='', name='')
        return data


public_api.add_resource(UserInfoAPI, '/users/<int:user_id>', endpoint='public_user')
