# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSameTree(r1, r2):
            if not r1 and not r2:
                return True
            
            r1val = r1.val if r1 else None
            r2val = r2.val if r2 else None
        
            if r1val != r2val:
                return False

            return isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)
        
        return isSameTree(p, q)
