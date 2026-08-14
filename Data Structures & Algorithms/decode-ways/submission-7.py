class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def Tcount(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            count = 0        
            count = Tcount(i+1)
            
            if i+1 < n:
                if s[i] == "1" or (s[i] == "2"and s[i+1] in "0123456"):
                    count += (Tcount(i+2))
            memo[i] = count
            return count
        
        return Tcount(0)
        

