class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rightMax = height[n-1]
        leftMax = height[0]
        left = 0
        right = n-1
        totalWater = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                totalWater += max(0,leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                totalWater += max(0,rightMax - height[right])
        
        return totalWater
