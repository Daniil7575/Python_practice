def month_name(month, lang):

    months_ru = ["январь", "февраль", "март", "апрель", "май", "июнь",
                 "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

    months_en = ["january", "february", "march", "april", "may", "june",
                 "july", "august", "september", "october", "november",  "december"]

    return months_ru[month - 1] if lang == "ru" else months_en[month - 1]


# print(month_name(int(input()), input()))
