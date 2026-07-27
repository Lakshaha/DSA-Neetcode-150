class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def check(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True
        
        def dfs(i):
            if i == len(s):
                res.append(part[:])
                return
            
            for end in range(i,len(s)):
                if check(i,end):
                    part.append(s[i:end+1])
                    dfs(end+1)
                    part.pop()
        
        dfs(0)
        return res