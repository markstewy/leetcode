# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        if self.isSametree(root, subroot):
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

    
    def isSametree(self, root, subroot):
        if subroot == None and root == None:
            return True
        if root and subroot and root.val == subroot.val:
            return self.isSametree(root.left, subroot.left) and self.isSametree(root.right, subroot.right)
        else:
            return False
