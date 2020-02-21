def permute(text):

    out = []

    # base case
    if len(text) == 1:
        out = [text]

    else:

        # for every letter in string

        for i, let in enumerate(text):

            # for every permutation resulting from step2 and step3
            for perm in permute(text[:i] + text[i+1:]):

                # add it to the output
                print(f"current letter is {let}")
                print(f"current perm is {perm}")
                out += [let+perm]

    return out


print(permute("abc"))
