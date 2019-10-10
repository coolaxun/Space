from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from app.common.exceptions import ValidationError
from app.common.errors import bad_request
from app.serve import serve_blue


@serve_blue.errorhandler(ValidationError)
def validation_error(e):
    msg = 'unknown error'
    if e.args:
        msg = e.args[0]
    return bad_request(msg)


@serve_blue.errorhandler(404)
def not_found(e):
    response = jsonify({'message': 'not found data'})
    response.status_code = 404
    return response


@serve_blue.errorhandler(Exception)
def unknown_error(e):
    response = jsonify({'message': 'unknown error'})
    response.status_code = 500
    return response
