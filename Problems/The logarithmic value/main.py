import math

num1, num2 = [int(input()) for _ in range(2)]

if num2 > 1:
    print(round(math.log(num1, num2), 2))
else:
    print(round(math.log(num1), 2))
