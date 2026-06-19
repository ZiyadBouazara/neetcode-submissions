class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        l, r = 0, 1
        profit = 0
        while r <= len(prices) - 1:
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
        
        # prices = [10,1,5,6,1,10]