"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clonedMap = {}

        def bfs(currNode):
            if currNode in clonedMap:
                return clonedMap[currNode]
            newNode = Node(currNode.val)
            clonedMap[currNode] = newNode
            for currNode in currNode.neighbors :
                newNode.neighbors.append(bfs(currNode))
            
            return newNode
        
        return bfs(node)

        