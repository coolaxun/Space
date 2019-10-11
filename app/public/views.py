from flask_restful import Resource, Api

from app.models.article import Post
from app.public import public
from app.util.log import log

public_api = Api(public)


class PostInfoAPI(Resource):

    def get(self, post_id):
        post = Post.objects.filter(id=post_id).first()
        # user = User.query.filter_by(id=user_id).first()
        if post:
            data = dict(id=str(post.id), name=post.title)
        else:
            data = dict(id='none', name='none')
        return data


# public_api.add_resource(PostInfoAPI, '/posts/<string:post_id>', endpoint='public_post')
