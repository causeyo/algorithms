def unique_01(text):
    return len(set(text) == len(text))


def unique_02(text):

    chars = set()

    for letter in text:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True


print(unique_02('acds'))
