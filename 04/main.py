
print("Provide a crypto price")
crypto_price = int(input())
print("Provide a crypto name")
crypto_name = input()

crypto_prices = {"bitcoin": 3000, "ethereum": 200, "iota": 30, "nem": 10, "test": -1}

try:
    if crypto_name == "test":
        raise KeyError("Unable to handle this key")
    if crypto_price > crypto_prices[crypto_name]:
        print("Waiting for a better rate")
    else:
        print("Good price, let's make some deal")
except KeyError as e:
    print(e)
    print("Unable to find a key :(")
finally:
    print("I will be invoked!")