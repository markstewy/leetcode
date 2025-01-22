# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def helper(root1, root2):
            if root1 == None and root2 == None:
                return True
            
            if root1 and not root2 or root2 and not root1 or root1.val != root2.val:
                return False
            
            return (helper(root1.left, root2.right) and helper(root1.right, root2.left)) or (helper(root1.right, root2.right) and helper(root1.left, root2.left))
        
        return helper(root1, root2)

