# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        a = min(p.val, q.val)
        b = max(p.val, q.val)

        def helper(root):

            if root.val < a:
                return helper(root.right)
            if root.val > b:
                return helper(root.left)
            
            if a <= root.val <= b:
                return root
        
        return helper(root)
