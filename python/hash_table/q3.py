"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    b = e = max_len = 0
    unordered_set = set()
    while e < len(s):
        if s[e] not in unordered_set:
            unordered_set.add(s[e])
            e += 1
        else:
            max_len = max(max_len,e-b)
            unordered_set.remove(s[b])
            b += 1

    max_len = max(max_len,e-b)
    return max_len
