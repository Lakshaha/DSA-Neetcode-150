# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val: # p is the smaller node
            p,q = q,p

        def find(node, p, q):
            if not node:
                return None
            if q.val < node.val:
                return find(node.left, p, q)
            elif p.val > node.val:
                return find(node.right, p, q)
            return node
        
        return find(root,p,q)