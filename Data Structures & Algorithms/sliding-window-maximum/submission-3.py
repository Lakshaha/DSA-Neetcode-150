class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)
        left = 0
        maxVal = nums[0]
        index = 0
        for right in range(n):
            if  left <= index <= right:
                if nums[right] > maxVal:
                    maxVal = nums[right]
                    index = right
            else:
                maxVal = max(nums[left:right+1])
                index = nums.index(maxVal)
            if right-left+1 == k:
                result.append(maxVal)
                left += 1
                continue
        return result






        # for i in range(n-k+1):
        #     result.append(max(nums[i:i+k]))
        # return result