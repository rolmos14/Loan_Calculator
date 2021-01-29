guests = []

while True:
    name = input()
    if name == ".":
        break
    else:
        guests.append(name)

print(guests, len(guests), sep="\n")
