from flask import render_template, session

from . import main
from app.models import User


@main.route('/')
@main.route('/index')
def index():
    posts = User.query.all()
    return render_template('main/index.html', title='首页', name=session.get('name'), posts=posts)

