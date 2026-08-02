# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #keep the array[robCurrent, skipCurrent]
        def dfs(node):
            if not node:
                return [0,0]
            
            leftRob, leftSkip = dfs(node.left)
            rightRob, rightSkip = dfs(node.right)

            robCurr = node.val + leftSkip + rightSkip
            skipCurr = max(leftRob,leftSkip) + max(rightRob, rightSkip)
            return [robCurr, skipCurr]
        
        return max(dfs(root))
            
