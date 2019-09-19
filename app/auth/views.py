from flask import jsonify, request

from app.auth import auth_blue
from app.models import User
from app import db


@auth_blue.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return jsonify({'error': 'authorize fail'})
    token = user.generate_auth_token(3600)
    return jsonify({'token': token.decode('ascii'), 'code': 20000})


@auth_blue.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'error': 'user has existed'})
    new_user = User()
    new_user.username = username
    new_user.password = password
    db.session.add(new_user)
    db.session.commit()
    return {'success': 1, 'msg': '注册成功'}


@auth_blue.errorhandler(Exception)
def handle_error(e):
    return jsonify({'error': str(e)})
