"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    for l in s:
        dic[l] = dic.get(l,0) + 1

    length = 0
    for key,val in dic.items():
        length += (val/2)*2
        dic[key] = val % 2

    if 1 in dic.values():
        return 1 + length
    else:
        return length
