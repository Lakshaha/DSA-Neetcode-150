class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
        

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
        

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            
            node = node.children[ch]
            node.count += 1
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            
            node= node.children[ch]
        
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return True
        
        