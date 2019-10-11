import os
import re

from flask import g, request
from flask_httpauth import HTTPTokenAuth  # HTTPBasicAuth

from config import config
from app.models.admin import User
from app.common.errors import unauthorized

auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token):
    g.current_user = None
    url = request.path
    for i in config[os.getenv('Flask_config') or 'default'].White_list:
        if re.match(i, url):
            return True
    user = User.verify_auth_token(token)
    if not user:
        return False
    g.current_user = user
    return True


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


# auth = HTTPBasicAuth()
#
#
# @auth.verify_password
# def verify_password(username_or_token, password):
#     # first try to authenticate by token
#     user = User.verify_auth_token(username_or_token)
#     if not user:
#         # try to authenticate with username/password
#         user = User.query.filter_by(username=username_or_token).first()
#         if not user or not user.verify_password(password):
#             return False
#     g.user = user
#     return True
#
#
# @api.route('/token')
# @auth.login_required
# def get_auth_token():
#     token = g.user.generate_auth_token()
#     return jsonify({'token': token.decode('ascii')})
#
#