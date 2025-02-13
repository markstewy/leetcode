# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.nodeSet = set(nodes)
        self.lca = None

        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            total = l + r
            if root in self.nodeSet:
                total += 1

            if total >= len(self.nodeSet):
                self.lca = root
                return 0

            return total
        
        dfs(root)
        return self.lca
