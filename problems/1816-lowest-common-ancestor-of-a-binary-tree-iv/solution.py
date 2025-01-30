# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.lca = root
        self. nodes = [node.val for node in nodes]

        def containsCount(root):
            if not root:
                return 0
            if root.val in self.nodes:
                return (containsCount(root.left) + containsCount(root.right)) + 1
            else:
                return (containsCount(root.left) + containsCount(root.right)) + 0

        def helper(root):
            if not root:
                return
            if containsCount(root) == len(self.nodes):
                self.lca = root
            else:
                return
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return self.lca
                
