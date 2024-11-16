# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, mn, mx):
            if not root:
                return True
            if mn < root.val < mx:
                return helper(root.right, root.val, mx) and helper(root.left, mn, root.val)
            else:
                return False
        
        return helper(root, -float("infinity"), float("infinity"))
