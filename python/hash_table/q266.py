"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
#faster
def canPermutePalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    dic = {}
    for val in s:
        dic[val] = (1 + dic.get(val,0)) % 2

    return dic.values().count(1) <= 1

def canPermutePalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    dic = {}
    for val in s:
        dic[val] = 1 + dic.get(val,0)

    count = 0
    for val in dic.values():
        if val % 2 == 1:
            count += 1
        if count > 1:
            return False;

    return True
