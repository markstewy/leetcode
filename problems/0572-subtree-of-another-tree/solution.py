# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if self.helper(root, subroot):
            return True
        if root == None:
            return False
        
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)


    def helper(self, root1, root2):
        r1 = root1.val if root1 else None
        r2 = root2.val if root2 else None
        if r1 != r2:
            return False

        if root1 == None and root2 == None:
            return True

        return self.helper(root1.left, root2.left) and self.helper(root1.right, root2.right)
        
