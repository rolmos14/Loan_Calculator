import math

x = int(input())

sigmoid = math.exp(x) / (math.exp(x) + 1)

print(round(sigmoid, 2))
