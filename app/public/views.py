from flask_restful import Resource, Api

from app.models import User
from app.public import public

public_api = Api(public)


class UserInfoAPI(Resource):

    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            data = dict(id=user.id, name=user.username)
        else:
            data = dict(id='', name='')
        return data


public_api.add_resource(UserInfoAPI, '/users/<int:user_id>', endpoint='public_user')
