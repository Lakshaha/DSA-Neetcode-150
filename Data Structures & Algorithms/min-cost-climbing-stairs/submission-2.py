class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        def check(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(check(i+1), check(i+2))

            return memo[i]
        
        return min(check(0), check(1))