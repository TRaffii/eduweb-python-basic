def ask_for_meal():
    name = input("Provide meal name:")
    price = input("Provide meal price:")
    return name, float(price)


def ask_for_discount():
    discount = input("Provide discount level (%):")
    return int(discount)


def ask_for_filename():
    filename = input("Provide filename:")
    return filename
