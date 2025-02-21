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
        root = p
        while root.parent:
            root = root.parent

        self.lca = None

        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            total = l + r

            if root.val == p.val or root.val == q.val:
                total += 1
            
            if total == 2:
                self.lca = root
                return 0
            
            return total
        
        dfs(root)
        return self.lca




