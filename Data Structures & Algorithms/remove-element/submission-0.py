class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        right = n-1
        left = 0
        k = 0
        while left <= right:
            if nums[left] == val:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
            else:
                left += 1

        nums = nums[:left]
        return left
        
