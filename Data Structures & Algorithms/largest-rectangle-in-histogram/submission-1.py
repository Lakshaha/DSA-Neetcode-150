class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0
        for i,height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                idx = stack.pop()
                h = heights[idx]
                w = i if not stack else i - stack[-1] -1 
                maxArea = max(maxArea, h*w)
            stack.append(i)
        return maxArea
