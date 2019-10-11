from flask_restful import Resource, marshal_with
from app.models.admin import User
from ...common.fields import users_fields, user_fields


class UserAPI(Resource):

    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return {'user': user}

    def post(self, user_id):
        pass

    def put(self, user_id):
        pass


class UserListAPI(Resource):
    # method_decorators = [auth.login_required]

    @marshal_with(users_fields)
    def get(self):
        users = User.query.all()
        return {'users': users}
