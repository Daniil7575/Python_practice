from PIL import Image, ImageDraw
import random


def draw_authors_name():
    new_image = Image.new("RGB", (700, 100), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)

    # Д
    draw.rectangle([0, 0, 100, 100], fill=(0, 50, 120))
    draw.line((10, 55, 90, 55), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)
    draw.line((15, 55, 50, 10), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)
    draw.line((50, 10, 85, 55), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)
    draw.line((10, 55, 10, 95), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)
    draw.line((90, 55, 90, 95), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)

    # А
    draw.line((110, 95, 150, 5), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)
    draw.line((150, 5, 190, 95), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)
    draw.line((125, 55, 175, 55), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              width=5)

    # H
    draw.line((210, 95, 210, 5), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=5)
    draw.line((210, 55, 290, 55), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              width=5)
    draw.line((290, 95, 290, 5), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              width=5)

    # Я
    draw.ellipse((310, 10, 390, 40), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw.line((390, 15, 390, 95), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              width=5)
    draw.line((310, 95, 385, 35), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              width=5)

    new_image.save("26.4.jpg", "jpeg")


draw_authors_name()
