from app.db import db
from app.models.User import User
from app.auth.forms import RegisterForm
from flask import render_template, redirect, url_for, flash
from app.auth import auth

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful', 'success')
        # return redirect(url_for('auth.login'))  
    return render_template('register.html', form=form)  
        
