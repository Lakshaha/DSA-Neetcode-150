# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            is_good = 1 if node.val >= max_so_far else 0

            max_so_far = max(max_so_far, node.val)

            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)

            return is_good + left + right
        
        return dfs(root, root.val)