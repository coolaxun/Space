from flask import request
from flask_restful import Resource

from app.models.article import Post


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
