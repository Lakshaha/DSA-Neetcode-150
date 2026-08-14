# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0,0]
            
            leftSkip, leftRob = dfs(node.left)
            rightSkip, rightRob = dfs(node.right)

            currRob = node.val + leftSkip + rightSkip
            currSkip = max(leftSkip, leftRob) + max(rightSkip, rightRob)
            return [currSkip, currRob]
        
        return max(dfs(root))