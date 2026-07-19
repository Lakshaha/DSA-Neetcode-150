class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def bt(subset, currSum, i):
            if currSum == target:
                result.append(subset[:])
                return
            if i == len(nums) or currSum > target:
                return
            #take the same value
            subset.append(nums[i])
            bt(subset, currSum + nums[i], i)
            subset.pop()
            bt(subset, currSum, i+1)
        
        bt([], 0, 0)
        return list(result)