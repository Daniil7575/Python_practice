def line(s, t):
    t = t.split(";")

    print("True" if eval(s.replace("x", f" * {float(t[0])}")) == float(t[1]) else "False")


# line("3.5x+0", "2;7")