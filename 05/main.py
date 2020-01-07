

ski_jumpers = [{"Ryoyu Kobayashi": "JPN"},
               {"Kamil Stoch": "PL"},
               {"Stefan Kraft": "AU"},
               {"Robert Johansson": "NOR"},
               {"Piotr Żyła": "PL"},
               {"Johann Andre Forfang": "NOR"}]

for jumper in ski_jumpers:
    print(jumper)

index = 0
while index < len(ski_jumpers):
    print(ski_jumpers[index], ski_jumpers[index + 1])
    index += 2

for jumper in ski_jumpers:
    if list(jumper.keys())[0] == "Kamil Stoch":
        print(jumper)
        break

index = 0
number_of_jumpers = 3
while index < number_of_jumpers:
    print(ski_jumpers[index])
    index += 1

for jumper in ski_jumpers:
    if list(jumper.values())[0] == "PL":
        print(jumper)
        break

for jumper in ski_jumpers:
    if list(jumper.values())[0] == "NOR":
        print(jumper)

norwegians = [jumper for jumper in ski_jumpers if list(jumper.values())[0] == "NOR"]
print(norwegians)
