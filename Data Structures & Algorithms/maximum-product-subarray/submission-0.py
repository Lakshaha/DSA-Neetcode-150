class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        globalMax = nums[0]

        for i in range(1,len(nums)):
            tempMax = max(nums[i], currMax*nums[i], currMin*nums[i])
            currMin = min(nums[i], currMax*nums[i], currMin*nums[i])

            currMax = tempMax

            globalMax = max(currMax, globalMax)
        
        return globalMax