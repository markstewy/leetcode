# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBal = True

        def helper(root):
            if not root:
                return 0

            l = helper(root.left) + 1
            r = helper(root.right) + 1

            if abs(l - r) > 1:
                self.isBal = False
                return 0
            return max(l, r)

        helper(root)
        return self.isBal
