class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]

        def bfs(row, col):
            queue = deque()
            queue.append([row, col])
            visited[row][col] = 1
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]
            count = 0
            while queue:    
                r,c = queue.popleft()
                count += 1
                for i in range(4):
                    nr = dr[i] + r
                    nc = dc[i] + c
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        if grid[nr][nc] == 1 and not visited[nr][nc]:
                            queue.append([nr,nc])
                            visited[nr][nc] = 1
            
            return count
        
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    area =bfs(i,j)
                    maxArea = max(area, maxArea)
        
        return maxArea