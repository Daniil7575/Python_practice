def rhythm_check(phrases):
    alph = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    return "Парам пам-пам" if len(set(map(lambda x: tuple(i for i in x if i in alph), phrases))) == 1 else "Пам парам"


print(rhythm_check(input().split(" ")))
