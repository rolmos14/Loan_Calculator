numbers = []

while True:
    num = input()
    if num == ".":
        break
    else:
        numbers.append(float(num))

print(min(numbers))
