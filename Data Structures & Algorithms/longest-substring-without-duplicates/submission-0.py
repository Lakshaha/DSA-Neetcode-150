class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}

        left = 0
        n = len(s)
        maxLen = 0
        for right in range(n):
            count[s[right]] = count.get(s[right],0)+1
            if count.get(s[right],0) > 1:
                while count[s[right]] != 1:
                    count[s[left]] -= 1
                    left += 1
            
            maxLen = max(maxLen, right-left+1)

        return maxLen            