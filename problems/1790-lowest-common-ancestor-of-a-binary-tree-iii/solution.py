"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        self.p = p
        self.q = q
        self.lca = None

        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            total = l + r
            if root.val == self.p.val or root.val == self.q.val:
                total += 1
            
            if total > 1:
                self.lca = root
                return 0
            
            return total
        
        root = self.p
        while root.parent:
            root = root.parent
        dfs(root)

        return self.lca

