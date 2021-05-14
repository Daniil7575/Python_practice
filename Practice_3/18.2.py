def ask_password():
    password = "password"
    attempts = 0

    for i in range(3):
        user_pass = input()

        if user_pass != password:
            attempts += 1

        else:
            print("Пароль принят")
            return 0

    print("В доступе отказано")


ask_password()