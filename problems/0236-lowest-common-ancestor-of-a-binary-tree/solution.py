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
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            total = l + r

            if root.val == p.val or root.val == q.val:
                total += 1
            
            if total == 2:
                self.lca = root
                return 0
            
            return total
        
        helper(root)
        return self.lca
        

            
