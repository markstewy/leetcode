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
            if not (l < root.val < r):
                return False

            return helper(root.right, root.val, r) and helper(root.left, l, root.val)
        
        return helper(root, -float("infinity"), float("infinity"))
