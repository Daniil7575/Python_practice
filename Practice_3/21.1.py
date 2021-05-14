def from_string_to_list(string, container):
    string = string.split(" ")

    for i in range(string.count("")):
        string.remove("")

    for i in range(len(string)):
        container.append(int(string[i]))


# a = [1, 2, 3]
# print(id(a))
# from_string_to_list("1", a)
# print(a)
# print(*from_string_to_list("1 545 756 755", [77, "vasdasd"]))
