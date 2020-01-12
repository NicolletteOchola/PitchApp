import os
from .. import mail
from flask import render_template, url_for, flash, redirect, request, Blueprint, url_for, current_app
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Post, Comment
from app.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm)
import secrets
from PIL import Image
from flask_mail import Message
from ..email import mail_message

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
                
        flash('Your account has been created! You are now able to log in', 'success')
        # mail_message("Welcome to PitchRank","email/welcome_user",user.email,user=user)

        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)