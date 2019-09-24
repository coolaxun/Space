from flask_restful import Resource, Api

from app.serve.models import Post
from app.public import public
from app.util.log import log

public_api = Api(public)


class PostInfoAPI(Resource):

    def get(self, post_id):
        post = Post.objects.all().first()
        # user = User.query.filter_by(id=user_id).first()
        if post:
            data = dict(id=str(post.id), name=post.title)
        else:
            data = dict(id='', name='')
        log.info(data['id'])
        return data


public_api.add_resource(PostInfoAPI, '/posts/<int:post_id>', endpoint='public_post')
