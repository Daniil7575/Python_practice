def go_bet(horse, bet):
    global bet_horses

    if 0 < horse < 11 and bet > 0 and horse not in bet_horses:
        bet_horses.append(horse)
        print(f"Ваша ставка в размере {bet} на лошадь {horse} принята")

    else:
        print("Что-то пошло не так, попробуйте еще раз")


bet_horses = []

inp = input("")

while inp != "q":
    inp = inp.split(", ")

    go_bet(int(inp[0]), int(inp[1]))

    inp = input()
