def ask_for_meal():
    name = input("Provide meal name:")
    price = input("Provide meal price:")
    try:
        return name, float(price)
    except ValueError:
        print("Unable to add a product, you need to provide a valid price")
        return None, None


def ask_for_service():
    name = input("Provide service type:")
    price = input("Provide service price:")
    guests = input("Provide number of guests:")
    try:
        return name, float(price), guests
    except ValueError:
        print("Unable to add a service, you need to provide a valid price")
        return None, None, None


def ask_for_discount():
    discount = input("Provide discount level (%):")
    try:
        return int(discount)
    except ValueError:
        print("Unable to add a discount, you need to provide a valid discount value")
        return None


def ask_for_check_discount():
    overall_sum = input("Provide sum:")
    discount = input("Provide discount level (%):")
    try:
        return float(overall_sum), int(discount)
    except ValueError:
        print("Unable to check a discount, you need to provide valid values")
        return None, None


def ask_for_filename():
    filename = input("Provide a filename:")
    return filename
