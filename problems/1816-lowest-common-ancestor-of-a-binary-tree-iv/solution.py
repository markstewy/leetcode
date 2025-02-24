# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        k = len(nodes)
        vals = [node.val for node in nodes]
        nodeSet = set(vals)
        self.lca = None

        def helper(root):
            if not root:
                return 0

            l = helper(root.left)
            r = helper(root.right)
            total = l + r

            if root.val in nodeSet:
                total += 1
            
            if total == k:
                self.lca = root
                return 0
            
            return total
        
        helper(root)
        return self.lca

