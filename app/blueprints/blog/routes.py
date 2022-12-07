from . import bp as app
from flask import render_template

@app.route('/blog')
def blog():
    return render_template('blog.html.j2')
