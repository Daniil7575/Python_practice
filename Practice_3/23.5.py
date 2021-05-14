def same_by(characteristic, values):
    return True if len(set(map(characteristic, values))) == 1 else False


# values = [1, 2, 3, 4]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")