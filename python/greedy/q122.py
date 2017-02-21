class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_time,sell_time,profit = 0,0,0
        while buy_time < len(prices) and sell_time < len(prices):
            while buy_time < len(prices)-1 and prices[buy_time] >= prices[buy_time+1]:
                buy_time += 1
            sell_time = buy_time
            while sell_time < len(prices)-1 and prices[sell_time] <= prices[sell_time+1]:
                sell_time += 1
            profit += prices[sell_time] - prices[buy_time]
            buy_time = sell_time + 1

        return profit

class Solution(object):
    def maxProfit(self, prices):
        #transact as much as possible
        return sum([max(prices[i+1] - prices[i],0) for i in range(len(prices)-1)])
