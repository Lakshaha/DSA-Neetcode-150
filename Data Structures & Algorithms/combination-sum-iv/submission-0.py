class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def track(currSum):
            if currSum == target:
                return 1
            if currSum > target:
                return 0
            
            if currSum in memo:
                return memo[currSum]
            totalWays = 0
            for num in nums:
                totalWays += track(currSum + num)
            
            memo[currSum] = totalWays
            return totalWays
        
        return track(0)