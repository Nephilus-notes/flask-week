from . import bp as app
from app import db
from flask import render_template, request, url_for, redirect, flash
from .models import Car
from flask_login import current_user, login_required


@app.route('/') 
@login_required
def home():
    all_cars = Car.query.all()
    return render_template('home.html.j2', cars= all_cars, user=current_user)

@app.route('/about')
def about():
    return render_template('about.html.j2')

# create a dynamic route to get a single post based on it's id
@app.route('/car/id')
@login_required
def car_by_id(id):
    car = Car.query.get(int(id))
    return render_template('post_single.html.j2', car=car)

@app.route('/create_car', methods=["POST"])
@login_required
def create_car():
    title = request.form['inputTitle']
    make = request.form['inputMake']
    model = request.form['inputModel']
    year = request.form['inputYear']
    color = request.form['inputColor']
    price = request.form['inputPrice']
    new_car = Car(title=title, make=make, model=model, year=year, color=color, price=price, user_id=current_user.id)
    db.session.add(new_car)
    db.session.commit()
    flash('Car ad created!', 'success')
    return redirect(url_for('main.home')) # similar redirect without import, using the function name
    # return redirect('/blog/posts') # redirect imported from flask

@app.route('/user/cars') 
@login_required
def user_cars():
    user_cars = Car.query.filter_by(user_id=current_user.id)
    return render_template('user_cars.html.j2', cars= user_cars)
