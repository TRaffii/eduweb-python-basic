import view
from bill import Bill


def main():
    bill = Bill()
    action = "Start"

    while action != "End":
        action = input("What you want to do? [Add, Sum, Discount, Check, Save, End]: ")

        if action == "Add":
            name, price = view.ask_for_meal()
            bill.add_meal(name, price)
        elif action == "Sum":
            print(bill.calculate())
        elif action == "Discount":
            discount = view.ask_for_discount()
            print(bill.calculate_with_discount(discount))
        elif action == "Check":
            overall_sum, discount = view.ask_for_check_discount()
            print(Bill.check_discount(overall_sum, discount))
        elif action == "Save":
            filename = view.ask_for_filename()
            bill.print_to_file(filename)


if __name__ == '__main__':
    main()
