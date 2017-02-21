"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
def wordPattern(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    s = pattern
    l = str.split(" ")
    return map(s.find,s) == map(l.index,l)


def wordPattern2(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    str_arr = str.split(" ")
    dic = {}
    if len(str_arr) != len(pattern):
        return False
    for i,val in enumerate(pattern):
        if val not in dic:
            dic[val] = str_arr[i]
        else:
            if dic[val] != str_arr[i]:
                return False

    if len(dic) != len(set(dic.values())):
        return False

    return True
