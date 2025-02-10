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
        self.lca = None

        root = p
        while root.parent:
            root = root.parent

        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)

            curr = 1 if (p.val == root.val or q.val == root.val) else 0
            total = l + r + curr

            if total == 2 and not self.lca:
                self.lca = root

            return total
        
        helper(root)
        return self.lca
