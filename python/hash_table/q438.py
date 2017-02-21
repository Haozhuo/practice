"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    dic = {}
    ret = []
    l = 0
    r = 0
    count = len(p)
    for i in range(0,26):
        dic[chr(ord('a')+i)] = 0
    for c in p:
        dic[c] += 1

    while(r < len(s)):
        if dic[s[r]] > 0:
            count -= 1
        dic[s[r]] -= 1
        r += 1

        if count == 0:
            ret.append(l)

        if r - l == len(p):
            if dic[s[l]] >= 0:
                count += 1
            dic[s[l]] += 1
            l += 1

    return ret
