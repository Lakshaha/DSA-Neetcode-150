import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        left = 0
        maxLen = 0
        maxFreq = 0


        for right,char in enumerate(s):
            count[char] += 1
            maxFreq = max(count[char], maxFreq)

            while (right-left+1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right-left+1)
        return maxLen
