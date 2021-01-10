a, b = [int(input()) for _ in range(2)]

multiples_of_3 = []
for num in range(a, b + 1):
    if num % 3 == 0:
        multiples_of_3.append(num)

mean = sum(multiples_of_3) / len(multiples_of_3)
print(mean)
