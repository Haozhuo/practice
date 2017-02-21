"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ans = 0
    for l in s:
        ans ^= ord(l)
    for l in t:
        ans ^= ord(l)
    return chr(ans)

def findTheDifference2(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    dic = {}
    for l in s:
        dic[l] = dic.get(l,0) + 1

    for l in t:
        if l not in dic.keys():
            return l
        elif dic[l] == 0:
            return l
        else:
            dic[l] -= 1

    return "\0"