# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l = min(p.val, q.val)
        r = max(p.val, q.val)

        def helper(root):
            print(root.val)
            if l <= root.val <= r:
                return root
            if root.val < l:
                return helper(root.right)
            elif root.val > r:
                return helper(root.left)
        
        return helper(root)

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         self.lca = None

#         def dfs(root):
#             if not root:
#                 return 0
            
#             l = dfs(root.left)
#             r = dfs(root.right)
#             total = l + r

#             if root.val == p.val or root.val == q.val:
#                 total += 1
            
#             if total == 2:
#                 self.lca = root
#                 return 0
            
#             return total
        
#         dfs(root)
#         return self.lca
            














