class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n-k+1):
            result.append(max(nums[i:i+k]))
        return result