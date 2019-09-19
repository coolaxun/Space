from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from app.common.exceptions import ValidationError
from app.common.errors import bad_request
from app.serve import serve_blue


@serve_blue.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])


@serve_blue.errorhandler(404)
def not_found():
    response = jsonify({'error': 'not found data'})
    response.status_code = 404
    return response

