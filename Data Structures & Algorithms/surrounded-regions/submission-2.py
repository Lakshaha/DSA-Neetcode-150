class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(row,col,visited):
            if (row,col) in visited or board[row][col] == "X":
                return
            visited.add((row,col))
            board[row][col] = "E"
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if 0<=nr<rows and 0<=nc<cols:
                    dfs(nr,nc,visited)
            return
        
        #need the edges one only
        for i in range(rows):
            dfs(i,0,visited)
            dfs(i,cols-1, visited)
        
        for i in range(cols):
            dfs(0,i,visited)
            dfs(rows-1,i,visited)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"
        