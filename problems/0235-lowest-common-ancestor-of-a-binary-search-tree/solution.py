# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None

        def helper(root):
            if root == None:
                return
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                self.lca = root
                return
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return self.lca

