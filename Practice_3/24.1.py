import sys


print(any([i.count("0") > 0 or i.count(0) > 0 for i in list(map(lambda x: x.split(" "), [k for k in sys.stdin]))]))


# 64 33 79 56 78 70 45 71 82 3
# 96 27 8 36 72 14 91 10 21 65
# 95 28 91 23 78 38 21 50 64 37
# 97 54 94 6 1 17 37 19 78 58
# 69 58 35 1 70 24 60 17 3 11
# 48 9 13 23 82 49 79 55 29 53
# 9 2 67 90 1 17 34 55 49 63
# 98 98 23 71 66 57 15 94 34 81
# 58 37 32 29 10 19 53 46 95 19
# 41 24 95 47 58 17 74 69 62 4
