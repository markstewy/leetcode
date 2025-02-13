# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pval = p.val
        self.qval = q.val
        self.lca = None

        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            total = l + r
            if root.val == self.pval or root.val == self.qval:
                total += 1

            if total > 1:
                self.lca = root
                return 0
            
            return total
        
        dfs(root)
        return self.lca
            
            

