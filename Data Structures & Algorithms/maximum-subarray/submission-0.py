class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        globalMax = nums[0]
        def dfs(i):
            nonlocal globalMax
            if i == len(nums):
                return 0
            if (i) in memo:
                return memo[(i,currSum)]
            
            curMax = max(nums[i], nums[i] + dfs(i+1))
            globalMax = max(globalMax, curMax)

            memo[i] = curMax 
            return memo[(i)]
        
        dfs(0)
        return globalMax