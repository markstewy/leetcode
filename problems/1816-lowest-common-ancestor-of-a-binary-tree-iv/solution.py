# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nSet = set(nodes)

        def helper(node):

            if not node:
                return None

            if node in nSet:
                return node
            
            l = helper(node.left)
            r = helper(node.right)

            if l and r:
                return node
            if l:
                return l
            if r: 
                return r
            
        return helper(root)
  

