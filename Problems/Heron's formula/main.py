from math import sqrt

a, b, c = [int(input()) for _ in range(3)]

p = (a + b + c) / 2
S = sqrt(p * (p - a) * (p - b) * (p - c))

print(S)
