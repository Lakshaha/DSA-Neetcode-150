class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i,currSum):
            if i >= n:
                if currSum == target:
                    return 1
                return 0
            
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            
            add = dfs(i+1, currSum + nums[i])
            sub = dfs(i+1, currSum - nums[i])
            memo[(i,currSum)] = add + sub
            return memo[(i,currSum)]
        
        return dfs(0,0)