from PIL import Image


def make_anagliph(filename, delta):
    image = Image.open(filename)
    res = Image.new("RGB", image.size, (0, 0, 0))

    pixels_old = image.load()
    pixels_new = res.load()

    for j in range(image.size[1]):
        for i in range(image.size[0]):
            if i - delta < 0:
                pixels_new[i, j] = pixels_old[i, j]

            else:
                pixels_new[i, j] = (pixels_old[i - delta, j][0], pixels_old[i, j][1], pixels_old[i, j][2])

    res.save("res.jpg", "jpeg")


make_anagliph("30090.jpg", 0)
