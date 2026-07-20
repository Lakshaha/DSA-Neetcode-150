class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0
        n = len(s)
        def check(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count 
        
        for i in range(n):
            odd = check(i,i)
            even = check(i, i+1)
            totalCount += (odd + even)
        return totalCount
