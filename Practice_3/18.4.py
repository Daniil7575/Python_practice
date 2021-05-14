def bracket_check(test_string):
    if len(test_string) == 0:
        return True

    if test_string[0] != ")":
        bracket_count = 0

        for i in range(len(test_string)):

            bracket_count += 1 if test_string[i] == "(" else -1

    print("YES" if bracket_count == 0 else "NO")


# bracket_check("(()())")
