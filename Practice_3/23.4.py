import math


def find_distance_to_astr(x, y):
    return min([round(math.sqrt((x - r * (math.cos(t * math.pi / 10000) ** 3)) ** 2 +
                                ((y - r * (math.sin(t * math.pi / 10000) ** 3)) ** 2)), 4) for t in range(1, 20000)])


r = 1
print(find_distance_to_astr(0.75, 0), 0.75, 0)
