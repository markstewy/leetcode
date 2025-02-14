# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #RECURSION
        # self.q = q
        # self.p = p
        # self.lca = None

        # def helper(root):
        #     if not root:
        #         return 0
            
        #     l = helper(root.left)
        #     r = helper(root.right)
        #     total = l + r

        #     if root.val == self.p.val or root.val == self.q.val:
        #         total += 1
            
        #     if total > 1:
        #         self.lca = root
        #         return 0
            
        #     return total
        
        # helper(root)
        # return self.lca

        self.l = min(p.val, q.val)
        self.r = max(p.val, q.val)
        self.lca = None

        def helper(root):
            if self.l <= root.val <= self.r:
                self.lca = root
                return
            
            if root.val < self.l:
                helper(root.right)
            
            if root.val > self.r:
                helper(root.left)
        
        helper(root)
        return self.lca
            

