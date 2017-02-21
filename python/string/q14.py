def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    bound = min(map(len,strs))
    if bound == 0:
        return ""
    string = ""
    for i in range(0,bound):
        std = strs[0][i]
        for j in range(0,len(strs)):
            if strs[j][i] != std:
                break
            j += 1

        if j != len(strs):
            return string
        string += std

    return string
