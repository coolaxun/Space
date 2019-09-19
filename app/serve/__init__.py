from flask import Blueprint

serve_blue = Blueprint('serve', __name__)

from . import authentication, errors, views
