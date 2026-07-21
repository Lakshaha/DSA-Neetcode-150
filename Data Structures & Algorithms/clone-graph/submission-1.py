"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        
        def bfs(node):
            if not node:
                return None
            if node in cloneMap:
                return cloneMap[node]
            newNode = Node(node.val)
            cloneMap[node]=newNode

            for neig in node.neighbors:
                newNode.neighbors.append(bfs(neig))
            return newNode
        
        return bfs(node)
        

        