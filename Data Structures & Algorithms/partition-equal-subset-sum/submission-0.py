class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2 != 0:
            return False
        
        totalSum //= 2
        memo = {}
        n = len(nums)

        def dfs(i, currSum):
            if currSum == totalSum:
                return True
            if currSum > totalSum or i >= n:
                return False
            if (i,currSum) in memo:
                return memo[(i,currSum)]

            include = dfs(i+1, currSum + nums[i])
            exclude = dfs(i+1, currSum)

            memo[(i,currSum)] = include or exclude
            return memo[(i,currSum)]
        
        return dfs(0,0)