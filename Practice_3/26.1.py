from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)

    if color.lower() == "r":
        for i in range(256):
            draw.line((i * 2, 0, i * 2, 200), fill=(i, 0, 0), width=2)

    if color.lower() == "g":
        for i in range(256):
            draw.line((i * 2, 0, i * 2, 200), fill=(0, i, 0), width=2)

    if color.lower() == "b":
        for i in range(256):
            draw.line((i * 2, 0, i * 2, 200), fill=(0, 0, i), width=2)

    new_image.save("26.1.png", "PNG")


# gradient("b")
