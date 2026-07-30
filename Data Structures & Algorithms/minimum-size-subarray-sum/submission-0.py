class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        n = len(nums)
        minLen = float("inf")
        for right in range(n):
            currSum += nums[right]
            while currSum >= target:
                minLen = min(minLen, right-left+1) 
                currSum -= nums[left]
                left += 1
    
        return minLen if minLen != float("inf") else 0