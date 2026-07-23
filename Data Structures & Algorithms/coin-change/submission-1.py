class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        n = len(coins)

        def check(remSum):
            if remSum == 0:
                return 0
            if remSum in memo:
                return memo[remSum]
            if remSum < 0:
                return float("inf")
            res = float("inf")
            for i in coins:
                val = check(remSum-i)
                if val != float("inf"):
                    res = min(res, 1+val)
            
            memo[remSum] = res
            return memo[remSum]
        
        ans = check(amount)
        return ans if ans != float("inf") else -1

