def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    i,j = 0,len(s)-1
    while i < j:
        res1,res2 = s[i].isalnum(),s[j].isalnum()
        if res1 and res2:
            res3 = s[i].upper() == s[j].upper()
            if res3:
                i,j = i+1,j-1
            else:
                return False
        else:
            if res1:
                j -= 1
            elif res2:
                i += 1
            else:
                i,j =i+1,j-1
    return True
