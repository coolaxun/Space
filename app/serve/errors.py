from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from app.common.exceptions import ValidationError
from app.common.errors import bad_request
from app.serve import serve_blue


@serve_blue.errorhandler(ValidationError)
def validation_error(e):
    msg = e.args[0] if e.args else 'unknown error'
    return bad_request(msg)


@serve_blue.errorhandler(404)
def not_found(e):
    msg = str(e) if str(e) else '404 error'
    response = jsonify({'message': msg, 'success': 0})
    response.status_code = 404
    return response


@serve_blue.errorhandler(Exception)
def unknown_error(e):
    msg = str(e) if str(e) else 'unknown error'
    response = jsonify({'message': msg, 'success': 0})
    response.status_code = 500
    return response


@serve_blue.app_errorhandler(404)
def page_not_found(e):
    response = jsonify({'message': '404 error ', 'success': 0})
    response.status_code = 404
    return response


@serve_blue.app_errorhandler(500)
def internal_server_error(e):
    response = jsonify({'message': 'Internal server error(500)', 'success': 0})
    response.status_code = 500
    return response
