class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dfs(i,buy):
            if i >= n:
                return 0

            if (i,buy) in memo:
                return memo[(i,buy)]
            
            if buy == 1:
                buyCurr = dfs(i+1,0) - prices[i]
                skipCurr = dfs(i+1,1)
                memo[(i,buy)] = max(buyCurr, skipCurr)
            
            else:
                sellCurr = dfs(i+2, 1) + prices[i]
                skipCurr = dfs(i+1,0)
                memo[(i,buy)] = max(sellCurr, skipCurr)

            return memo[(i,buy)]
        
        return dfs(0,1)