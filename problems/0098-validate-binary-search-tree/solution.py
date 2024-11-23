# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, l, r):
            if not root:
                return True
            if l < root.val < r:
                return helper(root.left, l, root.val) and helper(root.right, root.val, r)
            else:
                return False
        
        return helper(root, -float("infinity"), float("infinity"))
