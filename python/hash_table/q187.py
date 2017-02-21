def findRepeatedDnaSequences(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    dic = {}
    for i in range(0,len(s)-9):
        dic[s[i:i+10]] = dic.get(s[i:i+10],0) + 1

    return filter(lambda x:dic[x] > 1,dic.keys())

#NOTE:Rolling Hash
See q187.cpp located in C++/bits
