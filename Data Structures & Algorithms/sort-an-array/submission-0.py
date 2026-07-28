class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        m = len(nums)//2
        val = nums[m]
        left = [x for x in nums if x < val]
        mid = [x for x in nums if x == val]
        right = [x for x in nums if x > val]
        
        return self.sortArray(left) + mid + self.sortArray(right)