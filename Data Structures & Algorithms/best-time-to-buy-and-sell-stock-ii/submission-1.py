class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        #buy == 1, you can buy if buy == 0 u cant buy
        memo = {}
        def dfs(i,buy):
            if i == len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            
            if buy == 1:
                buyYes = dfs(i+1,0) - prices[i]
                skip = dfs(i+1,1)
                memo[(i,buy)] = max(buyYes, skip)
            else:
                sellYes = dfs(i+1,1) + prices[i]
                skip = dfs(i+1,0)
                memo[(i,buy)] = max(sellYes, skip)
        
            return memo[(i,buy)]
        return dfs(0,1)

