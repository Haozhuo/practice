def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = {}
    for i in range(0,len(strs)):
        sorted_str = "".join(sorted(strs[i]))
        dic.setdefault(sorted_str,[])
        dic[sorted_str].append(strs[i])

    ret = []
    for val in dic.values():
        ret.append(val)

    return ret

#NOTE:Faster
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = collections.defaultdict(list)
    map(lambda x:dic["".join(sorted(x))].append(x),strs)
    return [val for val in dic.values()]
