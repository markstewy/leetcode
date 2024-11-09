# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.root = root
        
        def helper(node: TreeNode, leftBoundary: int, rightBoundary: int):
            if not node:
                return True
            
            if not leftBoundary < node.val < rightBoundary:
                return False
            
            return helper(node.left, leftBoundary, node.val) and helper(node.right, node.val, rightBoundary)
        
        return helper(root, -float("infinity"), float("infinity"))

        
        
