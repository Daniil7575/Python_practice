sequense = input()
max_cnt = 0
current_cnt = 0
for result in sequense:
    if result == "о":
        current_cnt += 1
    else:
        if current_cnt > max_cnt:
            max_cnt = current_cnt
            current_cnt = 0
print(max_cnt)
