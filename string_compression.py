def compress(text):

    output = ""
    length = len(text)

    if length == 0:
        return ""

    if length == 1:
        return text+"1"

    counter = 1
    i = 1

    while i < length:

        if text[i] == text[i-1]:
            counter += 1
        else:
            output = output + text[i-1] + str(counter)
            counter = 1

        i += 1

    output = output + text[i-1] + str(counter)

    return output


print(compress("AAB"))
