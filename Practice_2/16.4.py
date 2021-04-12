n = int(input())

stations = [[0 for j in range(n)] for i in range(n)]

for i in range(1, n):
    price = input().split(" ")
    for j in range(i):
        stations[i][j] = int(price[j])
        stations[j][i] = int(price[j])

start_end = input().split(" ")
start_end.sort()
min_st_numb = n + 1
min_cost = stations[int(start_end[1])][int(start_end[0])]

for i in range(n):
    for j in range(i):
        if stations[i][j] + stations[int(start_end[1])][i] < min_cost and i + 1 < min_st_numb:
            min_cost = stations[i][j] + stations[n - 1][j]
            min_st_numb = i

min_st_numb = start_end[0] if min_st_numb == n + 1 else min_st_numb

print(min_st_numb)
