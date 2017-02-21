"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
#Iteratively update
def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    ret = [0]*(rowIndex+1)
    ret[0] = 1
    for i in range(1,rowIndex+1):
        for j in range(i,0,-1):
            ret[j] += ret[j-1]
    return ret



#Math solution
def getRow2(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]

    ret = []
    numer = 1
    deno = 1
    for i in range(0,rowIndex+1):
        if i == 0 or i == rowIndex:
            ret.append(1)
        else:
            numer = numer * (rowIndex-i+1)
            deno = deno * i
            ret.append(numer/deno)

    return ret
