class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            val = 1
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]

                if 0<=nr<rows and 0<=nc<cols:
                    if matrix[nr][nc] > matrix[r][c]:
                        val = max(val, 1+dfs(nr,nc))
                
            memo[(r,c)] = val
        
            return memo[(r,c)]
        val = 0
        for i in range(rows):
            for j in range(cols):
                val = max(val, dfs(i,j))

        return val

                
                        
