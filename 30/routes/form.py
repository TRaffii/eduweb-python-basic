from flask import Blueprint, request, session, render_template

form_routes = Blueprint('form_routes', __name__)


@form_routes.route('/add_meal_form')
def add_meal_form():
    return render_template('add_meal_form.html')
