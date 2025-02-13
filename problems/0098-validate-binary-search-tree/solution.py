# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isBST = True

        def helper(root, lval, rval):
            if not root:
                return
            
            if lval < root.val < rval:
                helper(root.left, lval, root.val)
                helper(root.right, root.val, rval)
            else:
                self.isBST = False
                return
            
        helper(root, -float("infinity"), float("infinity"))
        return self.isBST
