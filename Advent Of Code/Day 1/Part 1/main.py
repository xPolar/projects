import os, sys
list = open(os.path.join(sys.path[0], "input.txt"), "r").read().split("\n")
fuel_required = 0
for number in list:
    try:
        fuel_required += int((float(number) / 3)) - 2
    except ValueError:
        pass
print(f"You will need a total of {fuel_required}")