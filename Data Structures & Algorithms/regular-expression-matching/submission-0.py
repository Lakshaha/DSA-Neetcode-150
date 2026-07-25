class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if j == len(p):
                return i == len(s)
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j+1) < len(p) and p[j+1] == "*":
                dontUse = dfs(i,j+2)
                use = match and dfs(i+1,j)
                memo[(i,j)] = use or dontUse
                return memo[(i,j)]
            
            if match:
                memo[(i,j)] = dfs(i+1,j+1)
                return memo[(i,j)]
            
            memo[(i,j)] = False
            return memo[(i,j)]
        
        return dfs(0,0)

