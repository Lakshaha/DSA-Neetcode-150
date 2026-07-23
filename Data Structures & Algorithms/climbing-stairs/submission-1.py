class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        def check(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = check(i+1) + check(i+2)
            return dp[i]
        
        return check(0)
            