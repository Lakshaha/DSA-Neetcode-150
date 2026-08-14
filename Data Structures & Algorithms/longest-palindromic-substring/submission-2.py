class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def check(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        result = ""
        for i in range(n):
            odd = check(i,i)
            even = check(i,i+1)
            if len(result) < len(odd):
                result = odd[:]
            if len(result) < len(even):
                result = even[:]
            

        
        return result
            