def create_frac_tree():
    global wb_tree
    black = []
    white = []

    [black.append(white) for i in range(3)]
    [white.append(black) for i in range(2)]

    wb_tree.append(black)


wb_tree = []
create_frac_tree()
