"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
def numberOfBoomerangs(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    num = 0
    for p1 in points:
        dic = {}
        for p2 in points:
            f = p1[0] - p2[0]
            s = p1[1] - p2[1]
            dic[f*f+s*s] = 1 + dic.get(f*f+s*s,0)

        for val in dic.values():
            num += val * (val - 1)
    return num
