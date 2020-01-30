def finder(arr1, arr2):

    for element in arr1:
        if element not in arr2:
            print(element)
            return element


# finder([1,2,3,4],[3,2,4])


def finder_01(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

import collections

def finder_02(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr1:
        d[num]+=1

    for num in arr2:
        if d[num]==0:
            return num
        else:
            d[num]-=1

def clever_finder(arr1, arr2):
    result = 0

    # perform an XOR between the numbers in arrays
    for num in arr1+arr2:
        result ^= num

    return result

clever_finder([1,2,3,4],[3,2,4])