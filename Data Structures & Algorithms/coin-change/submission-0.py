class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        memo = {}
        def dfs(remSum):
            if remSum in memo:
                return memo[remSum]
            if remSum == 0:
                return 0
            if remSum < 0:
                return float("inf")
            res = float("inf")
            for i in coins:
                val = dfs(remSum-i)
                if val != float("inf"):
                    res = min(res, 1+val)
                
            
            memo[remSum] = res
            return res
        ans = dfs(amount)
        return ans if ans != float("inf") else  -1


            