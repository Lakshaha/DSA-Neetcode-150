from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        array = deque()
        result = []
        left = 0
        for right, num in enumerate(nums):
            while array and array[0] < left:
                array.popleft() #remove element if not in window
            
            while array and nums[array[-1]] < nums[right]:
                array.pop() #remove element from back if not a max element
            
            array.append(right)
            if right-left+1 == k:
                result.append(nums[array[0]])
                left += 1

        return result
