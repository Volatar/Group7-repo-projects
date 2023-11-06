from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
import json
import os
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if os.path.exists('user_data.json'):
            file = open("user_data.json", 'r')
            user_data = json.load(file)
            file.close()
        else:
            user_data = {}

        if email in user_data:
            flash('Email already exists.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            user = {'email': email, 'name': first_name, 'password': password1}
            user_data[email] = user
            file = open("user_data.json", 'w')
            file.write(json.dumps(user_data, indent=4))
            file.close()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if os.path.exists('user_data.json'):
            file = open("user_data.json", 'r')
            user_data = json.load(file)
            file.close()
        else:
            user_data = {}

        if email in user_data:
            user = user_data.get(email)
            if user['password'] == password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
