class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0

        for num in nums:
            if num-1 not in nums:
                currLen = 1
                currNum = num
                while currNum + 1 in nums:
                    currLen += 1
                    currNum += 1
            
                maxLen = max(maxLen, currLen)
        
        return maxLen