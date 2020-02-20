def permute(text):

    out = []

    # base case
    if len(text) == 1:
        out = [text]

    else:

        # for every letter in string

        for i, let in enumerate(text):

            # for every permutation resulting from step2 and step3
            for perm in permute(text[:1] + text[i+1:]):

                # add it to the output
                out += [let+perm]

    return out

print(permute("abc"))
