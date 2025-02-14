# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxLevel = 0

        def helper(root, level):
            if not root:
                return
            
            self.maxLevel = max(level, self.maxLevel)
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root, 1)
        return self.maxLevel
