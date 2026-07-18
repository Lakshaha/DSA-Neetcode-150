# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        array = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            array.append(node.val)
            inorder(node.right)
        

        inorder(root)
        for i in range(len(array) - 1):
            if array[i] >= array[i + 1]:
                return False
            
        return True
            