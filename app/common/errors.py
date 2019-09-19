from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def make_error_rep(code, message=None, **kwargs):
    if message is None:
        message = HTTP_STATUS_CODES.get(code, 'an error')

    response = jsonify(code=code, message=message, **kwargs)
    return response


def make_response(code, data=None):
    data = data if data else []
    response = jsonify(code=code, data=data)
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def unauthorized(message):
    response = jsonify({'error': 'Unauthorized', 'message': message})
    response.status_code = 401
    return response


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response
