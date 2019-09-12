from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from app.models import User
from .. import db


@main.route('/')
@main.route('/index')
def index():
    posts = User.query.all()
    return render_template('main/index.html', title='首页', name=session.get('name'), posts=posts)

