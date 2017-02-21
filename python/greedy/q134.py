class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total,pos,net_vol = 0,0,0
        for i in range(len(cost)):
            net_vol += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if(net_vol < 0):
                net_vol = 0
                pos = i + 1

        if total >= 0:
            return pos
        return -1
