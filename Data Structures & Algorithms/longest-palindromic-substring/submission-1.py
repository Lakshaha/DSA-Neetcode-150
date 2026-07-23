class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        n = len(s)
        def check(left,right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        for i in range(n):
            #odd lenths, even lenghts
            odd = check(i,i)
            even = check(i,i+1)

            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result