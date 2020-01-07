from meal import Meal
from service import Service


class Bill:

    def __init__(self):
        self.entries = []

    @staticmethod
    def check_discount(overall_sum, discount):
        return overall_sum - overall_sum * discount/100

    def calculate_with_discount(self, discount):
        current_sum = self.calculate()
        return current_sum - current_sum * discount/100

    def calculate(self):
        cost = 0.0
        for meal in self.entries:
            cost += meal.price
        return cost

    def print_to_file(self, filename):
        with open(filename, "w") as file:
            for meal in self.entries:
                file.write("Product name: {}, price: {} \n".format(meal.name, meal.price))

    def add_meal(self, name, price):
        meal = Meal(name, price)
        self.entries.append(meal)

    def add_service(self, name, price, guest_number):
        service = Service(name, price, guest_number)
        self.entries.append(service)
