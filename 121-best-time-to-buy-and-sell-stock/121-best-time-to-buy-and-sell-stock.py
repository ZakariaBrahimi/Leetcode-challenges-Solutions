class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left  = 0 # buy
        right = 1 # sell
        profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left] # = 4 - 1 = 3
                if currentProfit > profit:
                    profit = currentProfit
            else:
                left = right
            right += 1
        return profit
        