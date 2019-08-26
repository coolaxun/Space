import os
import re

from flask import g, jsonify, request
from flask_httpauth import HTTPTokenAuth  # HTTPBasicAuth

from app.models import User
from app.v1 import api
from app.v1.errors import forbidden, unauthorized
from config import config

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


@api.route('/login', methods=['POST'])
def login():
    print('ok')
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print('username:' + username if username else '')
    print('password:'+ password if username else '')
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return jsonify({'error': 'Unauthorized Access'})
    g.user = user
    token = user.generate_auth_token(3600)
    return jsonify({'token': token.decode('ascii'), 'code': 20000})


@api.before_request
@auth.login_required
def before_request():
    url = request.path
    for i in config[os.getenv('Flask_config') or 'default'].White_list:
        if re.match(i, url):
            return
    if not g.current_user:
        return forbidden('Unconfirmed account')
    # if not g.current_user or not g.current_user.confirmed:
    #     return forbidden('Unconfirmed account')


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.route('/hello')
@auth.login_required
def hello():
    return jsonify({'k': 'hello'})

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
