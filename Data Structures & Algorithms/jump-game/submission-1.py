class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        n = len(nums)
        for i,jump in enumerate(nums):
            if i > farthest:
                return False
            
            farthest = max(i+jump, farthest)

            if farthest >= n:
                return True
        
        return True

