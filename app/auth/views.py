from flask import render_template, redirect, request, url_for, flash
# from flask_login import login_user, login_required, logout_user

from app.auth import auth
# from app.auth.forms import LoginForm
from app.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    pass
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     print(user)
    #     if user is not None and user.verify_password(form.password.data):
    #         login_user(user, form.remember_me.data)
    #         return redirect(request.args.get('next') or url_for('auth.admin'))
    #     # flash('Invalid username or password.')
    # return render_template('auth/login.html', form=form, title='Login')
#
#
# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out')
#     return redirect(url_for('main.index'))
#
#
# @auth.route('/admin')
# @login_required
# def admin():
#     return render_template('auth/admin.html')
