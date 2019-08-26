from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from app.common.exceptions import ValidationError
from app.v1 import api


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])


@api.errorhandler(404)
def not_found():
    return jsonify({'error': 'not found data'})


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


def make_response():
    pass