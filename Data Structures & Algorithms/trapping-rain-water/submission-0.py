class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        totalArea = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                totalArea += max(0,leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                totalArea += max(0,rightMax-height[right])
        return totalArea

