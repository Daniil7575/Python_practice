def print_only_new(message):
    global jokes
    prev_len = len(jokes)
    jokes.add(message)

    if len(jokes) != prev_len:
        print(message)


jokes = set()
inp = input()

while inp != "q":
    print_only_new(inp)

    inp = input()
