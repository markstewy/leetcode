# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def helper(node):
            if not node:
                return 0
            
            l = helper(node.left)
            r = helper(node.right)
            if abs(l - r) > 1:
                self.isBalanced = False
            
            return 1 + max(l, r)

            
        helper(root)
        return self.isBalanced
