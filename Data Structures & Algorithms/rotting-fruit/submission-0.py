class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #add the dirty one
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visit.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1
            
        if fresh == 0:
            return 0
        time = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = 2
                dr = [1,-1,0,0]
                dc = [0,0,1,-1]

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr,nc) not in visit:
                        grid[nr][nc] = 2
                        fresh -= 1
                        visit.add((nr,nc))
                        queue.append((nr,nc))
            time += 1
        
        return time-1 if fresh == 0 else -1
                    