from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from .forms import RegistrationForm, LoginForm
from app.models.User import User
from app.db import db
from ..auth import auth

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RegistrationForm() 
    if form.validate_on_submit():
        print("what?")
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Username already exists. Please choose another one.', 'danger')
            return render_template('auth/register.html', form=form)
        
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()


        login_user(user)
        return redirect(url_for('main.home'))
    
    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = LoginForm() 
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Invalid username or password.', 'danger')
    
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('auth/login.html', form=form, current_time=current_time)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@auth.route('/forgot-password')
def forgot_password():
    return render_template('auth/forgot_password.html')