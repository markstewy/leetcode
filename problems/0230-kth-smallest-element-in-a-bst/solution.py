# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ino = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            
            self.ino.append(root.val)
            if len(self.ino) == k:
                return
            
            inorder(root.right)
        
        inorder(root)
        
        return self.ino[k - 1]
            

