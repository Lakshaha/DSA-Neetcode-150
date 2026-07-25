class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        if len(s1) + len(s2) != len(s3):
            return False
        
        def dfs(i,j):
            if i>len(s1) or j>len(s2):
                return 0
            
            if i+j == len(s3):
                return True
            
            if (i,j) in memo:
                return memo[(i,j)]
            k = i+j
            val1 = False
            val2 = False
            if i < len(s1) and s1[i] == s3[k]:
                val1 = dfs(i+1,j)
            if j < len(s2) and s2[j] == s3[k]:
                val2 = dfs(i,j+1)
            
            memo[(i,j)] = val1 or val2
            return memo[(i,j)]
        return dfs(0,0)

