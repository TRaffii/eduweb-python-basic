from flask import Blueprint, request, session
from bill import Bill

logic_routes = Blueprint('logic_routes', __name__)


@logic_routes.route('/add_meal', methods=['POST'])
def add_meal():
    bill = get_bill()

    name = request.form['meal_name']
    price = float(request.form['meal_price'])
    bill.add_meal(name, price)
    session['entries'] = bill.entries
    return "Success"


@logic_routes.route('/sum')
def sum():
    bill = get_bill()
    return f"Overall sum: {bill.calculate()}"


@logic_routes.route('/check', methods=['POST'])
def check():
    overall_sum = request.form['overall_sum']
    discount = float(request.form['discount'])
    value = Bill.check_discount(overall_sum, discount)
    return f"Whole order will cost: {value} after discount"


@logic_routes.route('/save/<filename>')
def save(filename):
    bill = get_bill()
    try:
        bill.print_to_file(filename)
        return "Success!"
    except:
        return "Unable to save the file"


def get_bill():
    bill = Bill()
    if 'entries' in session:
        entries = session['entries']
        bill.entries = entries
    return bill
