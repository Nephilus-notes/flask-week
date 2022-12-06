from app import app
from app.models import User, Car
from flask import render_template

@app.route('/') 
def home():
    return render_template('home.html.j2')

@app.route('/about')
def about():
    return render_template('about.html.j2')

@app.route('/blog')
def blog():
    return render_template('blog.html.j2')

@app.route('/register')
def register():
    return render_template('register.html.j2')

@app.route('/signin')
def sign_in():
    return render_template('signin.html.j2')

@app.route('/cars')
def cars():
    all_cars = Car.query.all()
    return render_template('cars.html.j2', all_cars=all_cars)



car_data = {
    0: {
        "name": "Maruti Swift Dzire VDI",
        "year": 2014,
        "selling_price": 450000
    },
    1: {
        "name": "Skoda Rapid 1.5 TDI Ambition",
        "year": 2014,
        "selling_price": 370000
    },
    2: {
        "name": "Honda City 2017-2020 EXi",
        "year": 2006,
        "selling_price": 158000
    }
}

@app.route('/api/cars/<id>')
def get_car_by_id(id):
    id = int(id)
    if id in car_data:
        context = { 
        'year': car_data[id]['year'],
        'name' : car_data[id]['name'],
        'selling_price': car_data[id]['selling_price']
        }

        return render_template('car_data.html', **context)