class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(row, col, visited, prevHeight):
            if (row,col) in visited or heights[row][col] < prevHeight:
                return
            
            visited.add((row,col))
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]
                if 0<=nr<rows and 0<=nc<cols:
                    dfs(nr,nc,visited,heights[row][col])
        
        for i in range(cols):
            dfs(0,i,pac,heights[0][i])
            dfs(rows-1,i,atl,heights[rows-1][i])
        
        for i in range(rows):
            dfs(i,0,pac,heights[i][0])
            dfs(i,cols-1, atl, heights[i][cols-1])
        
        return list(pac & atl)


