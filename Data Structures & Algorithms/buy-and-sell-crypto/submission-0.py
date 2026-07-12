class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currPrice = prices[0]
        n = len(prices)
        for i in range(n):
            currPrice = min(currPrice, prices[i])
            profit = max(profit, prices[i]-currPrice)
        
        return profit