from app import app
from app.models import User, Car
from flask import render_template


@app.route('/cars')
def cars():
    all_cars = Car.query.all()
    return render_template('cars.html.j2', all_cars=all_cars)

# @app.route('/api/cars/<id>')
# def get_car_by_id(id):
#     id = int(id)
#     if id in car_data:
#         context = { 
#         'year': car_data[id]['year'],
#         'name' : car_data[id]['name'],
#         'selling_price': car_data[id]['selling_price']
#         }

#         return render_template('car_data.html', **context)