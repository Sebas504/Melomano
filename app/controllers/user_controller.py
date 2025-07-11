# app/controllers/user_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, current_app, session, flash
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import os

from app.models.user_model import get_user_by_email, insert_user, get_user_basic_profile

user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()


@user_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('user_bp.login'))

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = current_app.connection
        user = get_user_by_email(connection, email)
        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect(url_for('user_bp.profile'))
        else:
            return "Login Failed"

    return render_template('login.html')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    connection = current_app.connection

    if request.method == 'POST':
        name = request.form['name']
        apellido = request.form['apellido']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        insert_user(connection, name, apellido, email, password)
        return redirect(url_for('user_bp.login'))
    return render_template('register.html')

@user_bp.route('/index')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_bp.login'))

    user = get_user_basic_profile(current_app.connection, user_id)
    return render_template('index.html', user=user)
