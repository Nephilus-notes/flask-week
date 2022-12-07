from . import bp as app
from flask import render_template

@app.route('/register')
def register():
    return render_template('register.html.j2')

@app.route('/signin')
def sign_in():
    return render_template('signin.html.j2')