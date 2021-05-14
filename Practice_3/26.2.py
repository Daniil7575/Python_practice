from PIL import Image, ImageDraw


def board(num, size):
    new_image = Image.new("1", (num * size, num * size), 0)
    draw = ImageDraw.Draw(new_image)

    for i in range(num ** 2):
        draw.rectangle([size * (i % num), size * (i // num), size * ((i % num) + 1), size * ((i // num) + 1)],
                       fill=((i % 2 + i // num) % 2) * (num + 1) % 2 + (i % 2)*(num % 2))

    new_image.save("26.2.png", "PNG")


board(6, 50)
