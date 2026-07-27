class Node:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
            
            node.word = word
        
        #all words added to the trie
        rows = len(board)
        cols = len(board[0])
        ans = []
        def dfs(r,c,node):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            nxt = node.children[ch]
            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None
            
            board[r][c] = "#"

            dr = [1,-1,0,0]
            dc = [0,0,1,-1]

            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != "#":
                    dfs(nr,nc,nxt)
            
            board[r][c] = ch

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root)
        
        return ans