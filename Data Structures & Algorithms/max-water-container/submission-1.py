class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = float("-inf")
        while left < right:
            currArea = (right-left) * min(heights[left], heights[right])
            maxArea = max(currArea, maxArea)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea
                
