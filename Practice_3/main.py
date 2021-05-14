from PIL import Image, ImageDraw

def asd():
    return list(map(lambda x : x + 40 if x + 40 <= 255 else x, (1, 2, 240)))

print(asd())
