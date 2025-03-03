# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isSub = False

        def helper(root, subRoot):
            if not root:
                return
            
            if isSameTree(root, subRoot):
                self.isSub = True
                return
            
            helper(root.left, subRoot)
            helper(root.right, subRoot)

        def isSameTree(root1, root2):
            r1val = root1.val if root1 else None
            r2val = root2.val if root2 else None

            if r1val != r2val:
                return False
            
            if not root1 and not root2:
                return True
            
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        helper(root, subRoot)
        return self.isSub
