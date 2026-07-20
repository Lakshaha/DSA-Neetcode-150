from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        def bfs(visited, row, col):
            queue = deque()
            queue.append([row, col])
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]
            visited[row][col] = 1
            while queue:
                row, col = queue.popleft()
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        if grid[nr][nc] == "1" and visited[nr][nc] == 0:
                            queue.append([nr,nc])
                            visited[nr][nc] = 1

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    bfs(visited, i, j)
                    count += 1

        return count