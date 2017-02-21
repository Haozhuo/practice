def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 0 or len(s) == 1:
        return s

    i,j = 0,len(s)-1
    l = list(s)
    while i < j:
        res1 = l[i] in "aeiouAEIOU"
        res2 = l[j] in "aeiouAEIOU"
        if res1 and res2:
            l[i],l[j] = l[j],l[i]
            i += 1
            j -= 1
        else:
            if not res1:
                i += 1
            if not res2:
                j -= 1

    return "".join(l)
