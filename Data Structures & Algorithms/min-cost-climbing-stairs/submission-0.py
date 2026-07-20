class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        # memo[0] = cost[0]
        # memo[1] = cost[1]
        def recurse(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return memo[i]

        return min(recurse(0), recurse(1))
        
