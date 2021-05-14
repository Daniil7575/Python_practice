def defractalize(fractal):
    [fractal.remove(i) for i in fractal if i == fractal]


# fractal = [2, 5]
# fractal.append(fractal)
# fractal.append(3)
# fractal.append(fractal)
# fractal.append(9)
# defractalize(fractal)
# print(fractal)
#
# fractal = [2, 5]
# fractal.append(fractal)
# fractal.append(3)
# defractalize(fractal)
# print(fractal)
