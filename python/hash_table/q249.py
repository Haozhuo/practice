"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        dic = {}
        for val in strings:
            dic[self.shift(val)] = dic.get(self.shift(val),[])
            dic[self.shift(val)].append(val)

        for li in dic.values():
            li.sort()
            ret.append(li)

        return ret

    def shift(self,s):
        temp = ""
        for i,l in enumerate(s[1:]):
            diff = ord(s[i]) - ord(s[i-1])
            if diff < 0:
                diff += 26
            temp += (chr(ord('a')+diff)+",")
        return temp
