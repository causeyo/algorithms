def paranthesis_check(text):

    if len(text) % 2 != 0:
        return False

    opening = set("({[")

    matches = set([("(", ")"), ("[", "]"), ("{", "}")])

    stack = []

    for paren in text:

        if paren in opening:
            stack.append(paren)

        else:

            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0

print(paranthesis_check("({)[]}"))