class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def bt(i, subset):
            if i == len(nums):
                result.append(subset[:])
                return 
            
            subset.append(nums[i])
            bt(i+1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            bt(i+1, subset)
        
        bt(0,[])
        return result