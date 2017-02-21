class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        bound = int(math.sqrt(n))
        l = [i*i for i in range(1,bound+1)]
        level = {n}
        count = 0

        while level:
            unit = set()
            count += 1
            for i in level:
                for j in l:
                    if i == j:
                        return count
                    if i < j:
                        break
                    unit.add(i-j)
            level = unit


        return count
