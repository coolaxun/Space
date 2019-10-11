from flask import jsonify

from app.serve import serve_blue
from app.auth.authentication import auth


@serve_blue.before_request
@auth.login_required
def before_request():
    pass
    # url = request.path
    # for i in config[os.getenv('Flask_config') or 'default'].White_list:
    #     if re.match(i, url):
    #         return
    # if not g.current_user:
    #     return forbidden('Unconfirmed account')
    # if not g.current_user or not g.current_user.confirmed:
    #     return forbidden('Unconfirmed account')


@serve_blue.route('/hello')
@auth.login_required
def hello():
    return jsonify({'k': 'hello'})
