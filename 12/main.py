from bill import Bill
from meal import Meal


def main():
    bill = Bill()
    bill.add_meal("Eggs", 6.99)
    bill.add_meal("Coffee", 3.99)

    print(bill.calculate())


if __name__ == '__main__':
    main()
