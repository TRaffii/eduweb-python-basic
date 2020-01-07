def ask_for_meal():
    name = input("Provide meal name:")
    price = input("Provide meal price:")
    return name, float(price)


def ask_for_service():
    name = input("Provide service type:")
    price = input("Provide service price (%):")
    guests = input("Provide number of guests:")
    return name, int(price), guests


def ask_for_discount():
    discount = input("Provide discount level (%):")
    return int(discount)


def ask_for_check_discount():
    overall_sum = input("Provide sum:")
    discount = input("Provide discount level (%):")
    return float(overall_sum), int(discount)


def ask_for_filename():
    filename = input("Provide filename:")
    return filename
