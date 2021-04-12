n = int(input())
m = int(input())

image = []

for i in range(n):
    image.append(input())

image = image[::2]

for i in range(len(image)):
    image[i] = image[i][::2]

for i in image:
    print(i)
