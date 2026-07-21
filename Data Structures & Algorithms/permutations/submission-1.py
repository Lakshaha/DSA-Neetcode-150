class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt(i):
            if i == len(nums):
                result.append(nums[:])
                return
            
            for j in range(i,len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                bt(i+1)
                nums[j], nums[i] = nums[i], nums[j]
                
            
        bt(0)
        return result