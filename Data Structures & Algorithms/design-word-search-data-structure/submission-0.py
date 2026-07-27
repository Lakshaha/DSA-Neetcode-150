class Node:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        
        node.isEnd = True
        

    def search(self, word: str) -> bool:

        def dfs(node, idx):
            if idx == len(word):
                return node.isEnd
            
            ch = word[idx]

            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(node.children[ch],idx+1)
            
            for ch in node.children:
                if dfs(node.children[ch],idx+1):
                    return True

            return False
        
        return dfs(self.root, 0)

        
