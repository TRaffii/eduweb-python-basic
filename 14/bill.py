from meal import Meal


class Bill:

    def __init__(self):
        self.meals = []

    def calculate_with_discount(self, discount):
        current_sum = self.calculate()
        return current_sum - current_sum * discount/100

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
