from . import bp as app
from app import db
from flask import render_template, url_for, request, redirect
from app.blueprints.main.models import User

@app.route('/register')
def register():
    return render_template('register.html.j2')

@app.route('/signin')
def sign_in():
    return render_template('signin.html.j2')

@app.route('/auth/create_user', methods=["POST"])
def create_user():
    username = request.form['inputUsername']
    email = request.form['inputEmail']
    first_name = request.form['inputFirstname']
    last_name = request.form['inputLastname']
    password = request.form['inputPassword']
    if email not in User.query.all():
        new_user = User(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.sign_in')) # similar redirect without import, using the function name
    # return redirect('/blog/posts') # redirect imported from flask
    else:
        return render_template('register_error.html.j2')