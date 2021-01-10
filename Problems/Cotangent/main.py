import math

angle = int(input())

angle_cotangent = 1 / math.tan(math.radians(angle))

print(round(angle_cotangent, 10))
