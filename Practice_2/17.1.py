alph = {"А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D",
        "Е": "E", "Ё": "E", "Ж": "ZH", "З": "Z", "И": "I",
        "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N",
        "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T",
        "У": "U", "Ф": "F", "Х": "KH", "Ц": "TC", "Ч": "CH",
        "Ш": "SH", "Щ": "SHCH", "Ы": "Y", "Э": "E", "Ю": "IU", "Я": "IA"}

line = input().replace("ь", "").replace("ъ", "").replace("Ь", "").replace("Ъ", "")

for i in line:
    if i.isupper():
        temp = alph[i]

        if len(alph[i]) > 1:
            temp = alph[i][1:]
            temp = alph[i][0] + temp.lower()
        line = line.replace(i, temp)

    elif i.islower():
        line = line.replace(i, alph[i.upper()].lower())

print(line)

