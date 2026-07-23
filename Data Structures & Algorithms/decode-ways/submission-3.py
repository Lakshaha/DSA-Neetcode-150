class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def check(i):
            if i == n:
                return 1
            
            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]
            
            ways = check(i+1)
            if i+1 < n:
                if s[i] == "1" or( s[i] == "2" and s[i+1] in "0123456"):
                    ways += check(i+2)
            
            memo[i] = ways
            return memo[i]
        
        return check(0)
