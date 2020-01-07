

def print_all(ski_jumpers):
    for jumper in ski_jumpers:
        print(jumper)


def find_jumper(jumper_name="Kamil Stoch"):
    for jumper in ski_jumpers:
        if list(jumper.keys())[0] == jumper_name:
            print(jumper)
            break


def find_by_nationality(ski_jumpers, nationality):
    for jumper in ski_jumpers:
        if list(jumper.values())[0] == nationality:
            print(jumper)
            break

def print_nice(*ski_jumpers):
    for jumper in ski_jumpers:
        print("\n************SKI JUMPER***********")
        print("************", jumper, "***********")
        print("************SKI JUMPER***********")

ski_jumpers = [{"Ryoyu Kobayashi": "JPN"},
               {"Kamil Stoch": "PL"},
               {"Stefan Kraft": "AU"},
               {"Robert Johansson": "NOR"},
               {"Piotr Żyła": "PL"},
               {"Johann Andre Forfang": "NOR"}]

# list all jumpers
print_all(ski_jumpers)
print_all(ski_jumpers)
find_jumper()
find_by_nationality(nationality="PL", ski_jumpers=ski_jumpers)

print(print_nice("Piotr  Żyła", "Timi Zajc", "test jumper"))
