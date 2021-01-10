import math

octahedron_edge_len = int(input())

area = 2 * math.sqrt(3) * math.pow(octahedron_edge_len, 2)
volume = 1 / 3 * math.sqrt(2) * math.pow(octahedron_edge_len, 3)

print(round(area, 2), round(volume, 2))
