word = input()
fav_num = input()
fav_lett = input()

if len(fav_lett) == 1:
    if fav_num.isdigit():
        fav_num = int(fav_num) - 1
        if len(word) >= fav_num:
            if word[fav_num] == fav_lett:
                print("ДА")
            else:
                print("HET")
        else:
            print("ОШИБКА")
    else:
        print("ОШИБКА")
else:
    print("ОШИБКА")
