# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def helper(root, mx):
            if not root: 
                return

            if root.val >= mx:
                self.count += 1

            helper(root.left, max(mx, root.val))
            helper(root.right, max(mx, root.val))
    
        helper(root, root.val)

        return self.count
