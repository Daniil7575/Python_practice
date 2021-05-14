from PIL import Image
import math


def make_preview(size, n_colors):
    image = Image.open("30090.jpg")
    new_image = Image.new("RGB", size, (0, 0, 0))

    pixels_old = image.load()
    pixels_new = new_image.load()

    ratio = image.size[0] / size[0], image.size[1] / size[1]

    for j in range(size[1]):
        for i in range(size[0]):
            pixels_new[i, j] = pixels_old[math.floor(i * ratio[0]), math.floor(j * ratio[1])]

    new_image = new_image.quantize(colors=n_colors, method=0, kmeans=0)

    new_image.save("res.bmp", "bmp")


# make_preview((500, 300), 3)
