class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        n = len(s)
        def check(left,right):
            while left >= 0 and right < n and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1
        
        for i in range(n):
            odd = check(i,i)
            even = check(i,i+1)
        
        return self.count
        
        