def swap(first, second):
    len_first = len(first)

    for i in range(len_first):
        second.append(first.pop(0))

    for i in range(abs(len(second) - len_first)):
        first.append(second.pop(0))


# fr = [1, 2, 3]
# sc = [4, 5, 6, 7]
# first_content = fr[:]
# second_content = sc[:]
# swap(fr, sc)
# print(fr, second_content, fr == second_content)
# print(sc, first_content, sc == first_content)
