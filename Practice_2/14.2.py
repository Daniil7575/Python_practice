# To: ivanov
# Сергей Иванов, ваш пароль слишком простой, смените
# его.
# To: polivanov
# Андрей Поливанов, ваш пароль слишком простой,
# смените

pass_name_DB = []
users_data_DB = []

inp = input()
while inp != "":
    users_data_DB.append(inp)
    inp = input()

for user in users_data_DB:
    temp = user.split(":")
    user_login = temp[0]
    user_name = temp[4].split(",")[0]
    user_pass = temp[1]
    pass_name_DB.append((user_login, user_name, user_pass))

bad_pass = input()
bad_pass_DB = bad_pass.split(";")

for i in pass_name_DB:
    if i[2] in bad_pass_DB:
        print(f"To: {i[0]}\n{i[1]}, ваш пароль слишком простой, смените его")
