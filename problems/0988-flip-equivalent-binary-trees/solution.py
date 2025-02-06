# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def helper(r1: TreeNode, r2: TreeNode):
            r1val = r1.val if r1 else None
            r2val = r2.val if r2 else None
            if r1val != r2val:
                return False
            if not r1 and not r2:
                return True

            return (helper(r1.left, r2.left) and helper(r1.right, r2.right)) or (helper(r1.right, r2.left) and helper(r1.left, r2.right))

        return helper(root1, root2)
