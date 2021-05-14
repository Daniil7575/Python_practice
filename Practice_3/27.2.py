from PIL import Image


# требуемая по условию функция
def image_filter_anti_aliasing(image, i, j):
    """ Усредняет цвет полученного пикселя и цвета соседей (в данном случае соседями являются пиксели на 1 уровне"""
    size = image.size
    pixels = image.load()

    r, g, b = 0, 0, 0
    neighbors = [pixels[i, j]]

    if i - 1 >= 0 and j - 1 >= 0:
        neighbors.append(pixels[i - 1, j - 1])

    if i - 1 >= 0:
        neighbors.append(pixels[i - 1, j])

    if i - 1 >= 0 and j + 1 < size[1]:
        neighbors.append(pixels[i - 1, j + 1])

    if j - 1 >= 0:
        neighbors.append(pixels[i, j - 1])

    if j + 1 < size[1]:
        neighbors.append(pixels[i, j + 1])

    if i + 1 < size[0] and j - 1 > 0:
        neighbors.append(pixels[i + 1, j - 1])

    if i + 1 < size[0]:
        neighbors.append(pixels[i + 1, j])
    if i + 1 < size[0] and j + 1 < size[1]:
        neighbors.append(pixels[i + 1, j + 1])

    for k in neighbors:
        r += k[0]
        g += k[1]
        b += k[2]

    count = len(neighbors)

    r, g, b = r // count, g // count, b // count

    return r, g, b


# функция, которая вызывает требуемую функцию для каждого пикселя картинки
# def anti_aliasing(image):
#     size = image.size
#     new_image = Image.new("RGB", size, (0, 0, 0))
#
#     pixels_old = image.load()
#     pixels_new = new_image.load()
#
#     # average_color = 0
#     #
#     # for z in range(size[1]):
#     #     for p in range(size[0]):
#     #         average_color += pixels_old[p, z][0] + pixels_old[p, z][1] + pixels_old[p, z][2]
#
#     resolution = size[0] * size[1]
#
#     # average_color //= resolution
#
#     for y in range(size[1]):
#         for x in range(size[0]):
#             pixels_new[x, y] = image_filter_anti_aliasing(image, x, y)
#
#     new_image.save("27.2.2.2.jpg", "jpeg")


# anti_aliasing(Image.open("30090.jpg"))
