import pizza_calculator


def main():
    price, dimension = input("Provide first pizza price and diameter separated by space\n").split()
    first_pizza_calculation = pizza_calculator.calculate_pizza_cm(float(price), int(dimension))
    price, dimension = input("Provide second pizza price and diameter separated by space\n").split()
    second_pizza_calculation = pizza_calculator.calculate_pizza_cm(float(price), int(dimension))

    if first_pizza_calculation > second_pizza_calculation:
        print("First pizza is a better deal!")
    else:
        print("Second pizza is a better deal!")


if __name__ == '__main__':
    main()

