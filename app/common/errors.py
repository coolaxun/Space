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







