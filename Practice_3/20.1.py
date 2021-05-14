def translate(text):
    global translatedText

    tmp = text.split(" ")

    dictionary = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я",
                  "А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я",
                  ",", ";", ":", "-", "\"", ".", "!", "?"]

    for i in range(len(tmp)):
        for j in tmp[i]:
            if j in dictionary:
                tmp[i] = tmp[i].replace(j, "")

    for i in range(tmp.count("")):
        tmp.remove("")

    translatedText = " ".join(tmp)


translatedText = None
translate(input())
print(translatedText)