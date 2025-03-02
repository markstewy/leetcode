# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True

        def helper(root1, root2):
            if not root1 and not root2:
                return

            r1val = root1.val if root1 else None
            r2val = root2.val if root2 else None

            if r1val != r2val:
                self.isSame = False
                return
            
            helper(root1.left, root2.left)
            helper(root1.right, root2.right)
        
        helper(p, q)
        return self.isSame
