"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1]]
    for i in range(1,numRows):
        res += [map(lambda x,y: x+y,res[-1]+[0],[0]+res[-1])]
    return res[:numRows]

def generate2(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ret = []
    for i in range(0,numRows):
        temp = []
        for j in range(0,i+1):
            if j == 0:
                temp.append(1)
            elif j == i:
                temp.append(1)
            else:
                temp.append(ret[i-1][j-1]+ret[i-1][j])
        ret.append(temp)

    return ret
