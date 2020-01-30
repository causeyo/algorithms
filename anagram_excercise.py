def anagram(text1, text2):
    """
    check if two strings are anagrams like below:

    "public relations" is an anagram of "crap built on lies."
    "clint eastwood" is an anagram of "old west action"

    :type text1: str
    :type text2: str
    :rtype: bool
    """
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()

    if len(text1) != len(text2):
        return False

    count_dict = {}

    for t in text1:
        if t in count_dict:
            count_dict[t] += 1
        else:
            count_dict[t] = 1

    for s in text2:
        if s in count_dict:
            count_dict[s] -= 1
        else:
            return False

    for letter in count_dict:
        if count_dict[letter] != 0:
            return False
    return True



anagram("clint eastwood", "old west action")
