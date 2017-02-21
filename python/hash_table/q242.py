"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    dic = {}
    for l in s:
        dic[l] = 1 + dic.get(l,0)

    for l in t:
        if l not in dic:
            return False
        elif dic[l] <= 0:
            return False
        else:
            dic[l] -= 1

    return True
