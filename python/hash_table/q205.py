"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return map(s.find,s) == map(t.find,t)

#Faster
def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dic = {}
    for i,val in enumerate(s):
        if val not in dic:
            dic[val] = t[i]
        else:
            if dic[val] != t[i]:
                return False
    return len(dic) == len(set(dic.values()))
