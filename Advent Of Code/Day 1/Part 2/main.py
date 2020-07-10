import os, sys
list = open(os.path.join(sys.path[0], "input.txt"), "r").read().split("\n")
fuel_required = 0
for number in list:
    try:
        part = int((float(number) / 3)) - 2
    except ValueError:
        pass
    else:
        fuel_required += part
        while (int(part / 3) - 2) > 0:
                part = int(part / 3) - 2
                fuel_required += part
print(f"You will need a total of {fuel_required}")