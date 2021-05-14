def find_farthest_orbit(orbits):
    orbits = [i for i in orbits if i[0] != i[1]]
    return [j for j in orbits if j[0] * j[1] == max([i[0] * i[1] for i in orbits])][0]


# orb = [(1, 3), (4, 6), (7, 2), (6, 6), (2.5, 10)]
# print(*find_farthest_orbit(orb))
