from meal import Meal


class Bill:

    def __init__(self):
        self.meals = []

    def add_discount(self):
        pass

    def calculate(self):
        cost = 0.0
        for meal in self.meals:
            cost += meal.price
        return cost

    def print_to_file(self):
        pass

    def add_meal(self, name, price):
        meal = Meal(name, price)
        self.meals.append(meal)
