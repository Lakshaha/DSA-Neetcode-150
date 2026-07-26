class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums[0]
        maxFreq = n//2
        currFreq = 0
        for i in range(1,n):
            
            if nums[i] == nums[i-1]:
                currFreq += 1
                if currFreq >= maxFreq:
                    return nums[i-1]
            else:
                currFreq =0
            
        return -1
