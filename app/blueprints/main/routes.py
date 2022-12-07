from . import bp as app
from app import db
from flask import render_template, request, url_for, redirect
from .models import Car


@app.route('/') 
def home():
    all_cars = Car.query.all()
    return render_template('home.html.j2', cars= all_cars)

@app.route('/about')
def about():
    return render_template('about.html.j2')

# @app.route('/')
# def cars():
    
# @app.route('/cars')
# def cars():
#     all_cars = Car.query.all()
#     return render_template('cars.html.j2', all_cars=all_cars)




# create a dynamic route to get a single post based on it's id
@app.route('/car/id')
def car_by_id(id):
    car = Car.query.get(int(id))
    return render_template('post_single.html.j2', car=car)

@app.route('/create_car', methods=["POST"])
def create_car():
    title = request.form['inputTitle']
    make = request.form['inputMake']
    model = request.form['inputModel']
    year = request.form['inputYear']
    color = request.form['inputColor']
    price = request.form['inputPrice']
    new_car = Car(title=title, make=make, model=model, year=year, color=color, price=price, user_id=2)
    db.session.add(new_car)
    db.session.commit()
    return redirect(url_for('main.home')) # similar redirect without import, using the function name
    # return redirect('/blog/posts') # redirect imported from flask


