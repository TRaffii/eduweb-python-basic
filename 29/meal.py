from entry import Entry


class Meal(Entry):

    def __init__(self, name, price):
        super().__init__(name, price)

    @classmethod
    def fromdict(self, dictionary):
        return_object = Meal(None, None)
        for k, v in dictionary.items():
            setattr(return_object, k, v)
        return return_object
