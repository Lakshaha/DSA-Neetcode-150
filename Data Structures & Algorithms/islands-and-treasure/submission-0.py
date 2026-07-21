class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #do bfs from every chest and it auto store distance
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visit.add((i,j))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist

                dr = [1,-1,0,0]
                dc = [0,0,1,-1]

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr,nc) not in visit:
                        queue.append((nr,nc))
                        visit.add((nr,nc))
                    
            dist += 1
        
        
