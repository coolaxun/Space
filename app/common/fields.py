from flask_restful import fields

signin_fields = {
    'token': fields.String(default=''),
    'success': fields.Integer(default=0),
    'message': fields.String(default='')
}

signup_fields = {
    'success': fields.Integer(default=0),
    'message': fields.String(default='register fail')
}

user_detail_fields = {
    'id': fields.Integer(attribute='id'),
    'username': fields.String(attribute='username'),
    'email': fields.String(attribute='email'),
    'phone': fields.String(attribute='phone'),
    'create_time': fields.DateTime(attribute='create_time'),
}

user_fields = {
    'user': fields.Nested(user_detail_fields, allow_null=True)
}

users_fields = {
    'users': fields.List(fields.Nested(user_detail_fields)),
}
