def rec_sum(n):
    """
    rec_sum(4) => 4+3+2+1
    """

    # BASE CASE
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

print(rec_sum(4))


def sum_func(n):
    """
     sum_func(4321) => 4+3+2+1
    """

    if n < 10:
        return n
    else:
        return n % 10 + sum_func(n // 10)

print(sum_func(4321))


def word_split(phrase, list_of_words, output=None):
    return output


print(word_split('themanran', ['the', 'man', 'ran']))
