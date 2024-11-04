# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def helper(n1, n2):
            if n1 == None and n2 == None:
                return True
            
            if (n1 == None) != (n2 == None) or n1.val != n2.val:
                return False
            
            return (helper(n1.left, n2.left) and helper(n1.right, n2.right)) or (helper(n1.left, n2.right) and helper(n1.right, n2.left)) 
        
        return helper(root1, root2)
