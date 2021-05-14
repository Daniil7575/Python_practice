def anagram_find(wrds):
    anagrams = []
    tmp = wrds[::]

    for i in range(len(wrds)):
        anagrams_of_word = []

        for j in range(-1, -len(tmp) + i, -1):
            if sorted([j.lower() for j in wrds[i]]) == sorted([k.lower() for k in tmp[j]]):
                if wrds[i].lower() in anagrams_of_word:

                    # добавляем слово в список
                    anagrams_of_word.append(tmp[j].lower())

                    # заменям его на спец. символ для избежания повторений и удалений из списка "налету"
                    tmp[j] = "#$^\""

                else:
                    anagrams_of_word.append(wrds[i].lower())
                    anagrams_of_word.append(tmp[j].lower())

                    tmp[j], tmp[i] = "#$^\"", "#$^\""

        if len(anagrams_of_word) > 0:
            anagrams.append(sorted(anagrams_of_word))

    return anagrams


for i in anagram_find([input() for i in range(int(input()))]):
    print(*i)
# 13
# окорок
# петлей
# Плетей
# рококо
# теплей
# Тишь
# ТОМНО
# тонко
# тонок
# тоном
# шить
# шьти
# ЬШИТ