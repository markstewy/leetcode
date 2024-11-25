# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = min(q.val, p.val)
        b = max(q.val, p.val)

        def helper(root):
            if a <= root.val <= b:
                return root
            elif b < root.val:
                return helper(root.left)
            elif a > root.val:
                return helper(root.right)
        
        return helper(root)
