# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.hasSub = False

        def isSameTree(r1, r2):
            if not r1 and not r2:
                return True
            
            r1val = r1.val if r1 else None
            r2val = r2.val if r2 else None

            if r1val != r2val:
                return False
            
            return isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)
        
        def helper(root):
            if isSameTree(root, subRoot):
                self.hasSub = True

            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)            
            
            return
        
        helper(root)
        return self.hasSub



