# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx,val in enumerate(inorder)}
        self.preIdx = 0
        def create(left, right):
            if left > right:
                return None 
            
            root_val = preorder[self.preIdx]
            root = TreeNode(root_val)
            self.preIdx += 1

            mid = inorder_map[root_val]
            root.left = create(left, mid-1)
            root.right = create(mid+1, right)
        
            return root
        
        return create(0, len(preorder)-1)
