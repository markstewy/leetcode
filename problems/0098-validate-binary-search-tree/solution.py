# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True

        def helper(root, l, r):
            if not root or not self.isValid:
                return
            
            if l < root.val < r:
                helper(root.left, l, root.val)
                helper(root.right, root.val, r)
            else:
                self.isValid = False
                return
            
        helper(root, -float("infinity"), float("infinity"))
        return self.isValid
