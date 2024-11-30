# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.a = min(p.val, q.val)
        self.b = max(p.val, q.val)

        def helper(root):
            if root.val < self.a:
                return helper(root.right)
            elif root.val > self.b:
                return helper(root.left)
            elif self.a <= root.val <= self.b:
                return root
    
        return helper(root)
