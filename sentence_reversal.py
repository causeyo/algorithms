def reversal_01(sentence):
    return " ".join(sentence.split()[::-1])


def reversal_02(sentence):
    return " ".join(reversed(sentence.split()))


def reversal_03(sentence):

    words = []
    length = len(sentence)
    spaces = [' ']

    i = 0

    while i < length:

        if sentence[i] not in spaces:

            word_start = i

            while i < length and sentence[i] not in spaces:

                i += 1

            words.append(sentence[word_start:i])

        i += 1

#  return " ".join(reversed(words))
# in case we do not want to use python 'reversed'

    output = ""
    length = len(words)

    while length > 0:

        output += words[length-1] + " "

        length -= 1

    return output.strip()


print(reversal_01("  I  like apples  "))
print(reversal_02("  I  like apples  "))
print(reversal_03("  I  like apples  "))
