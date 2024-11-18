# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subroot):
            if root == None and subroot == None:
                return True
            
            if root and subroot and root.val == subroot.val:
                return isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right)
            else:
                return False
        
        def helper(root, subroot):
            if not subroot:
                return True
            
            if not root:
                return False
            
            if isSameTree(root, subroot):
                return True
            
            return helper(root.left, subroot) or helper(root.right, subroot)
    
        return helper(root, subroot)

