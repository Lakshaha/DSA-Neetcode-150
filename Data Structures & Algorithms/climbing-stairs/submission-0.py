class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        count = 0

        def rec(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = rec(i+1) + rec(i+2)
            return dp[i]

        rec(0)
        
        return dp[0]