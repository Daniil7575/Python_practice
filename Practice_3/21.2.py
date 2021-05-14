def transpose(matrix):
    tmp_matrix = matrix[::]

    for i in range(len(tmp_matrix)):
        tmp = []

        for j in range(len(tmp_matrix[i])):
            tmp.append(tmp_matrix[j][i])

        matrix.append(tmp)
        matrix.pop(0)


# mtrx = [[1, 2], [3, 4]]
# transpose(mtrx)
# print(mtrx)
