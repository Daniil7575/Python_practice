import math


n0 = int(input())
thimbles = []
new_poses = []

for i in range(n0):
    thimbles.append(input())

k = int(input())

for i in range(k):
    thimbles_count = int(input())
    for j in range(thimbles_count):
        new_poses.append(int(input()) - 1)
    for z in range(len(new_poses)):
        thimbles.append(thimbles[new_poses[z]])

    thimbles = thimbles[math.ceil(len(thimbles)/2):]
    new_poses = []

for i in thimbles:
    print(i)

