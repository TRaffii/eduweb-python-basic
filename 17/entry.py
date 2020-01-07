

class Entry:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def generate_description(self):
        return "Product name: {}, price: {} \n".format(self.name, self.price)
