# Заявление на отпуск в период 1 июня – 20 июня. Иван Петров
# Заявление на отпуск в период 1 июня – 20 июня. Иван Петров
# Прошу выплатить 15 тысяч пиастров отпускных денег. Иван Петров
# На время отпуска в период 1 июня – 20 июня моим заместителем назначается Василий
# Васильев. Иван Петров


def setup_profile(name, vacation_dates):
    global current_employee
    global current_vac_dates
    current_employee = name
    current_vac_dates = vacation_dates


def print_application_for_leave():
    print(f"Заявление на отпуск в период {current_vac_dates}. {current_employee}")


def print_holiday_money_claim(summ):
    print(f"Прошу выплатить {summ} отпускных денег. {current_employee}")


def print_attorney_letter(name):
    print(f"На время отпуска в период {current_vac_dates} моим заместителем назначается {name}. {current_employee}")


current_employee = None
current_vac_dates = None

inp = input()

while inp != "q":
    eval(inp)
    inp = input()
