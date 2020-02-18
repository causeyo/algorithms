"""
FACTORIAL FUNCTION
n! = n * (n - 1)!

if n == 0, n! = 1

"""


def fact(n):

    # BASE CASE
    if n == 0:
        return 1
    else:
        return n * fact(n-1)