# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.ans = None

        def helper(root):
            if not root or self.i > k:
                return

            helper(root.left)
            self.i += 1
            if self.i == k:
                self.ans = root.val
            helper(root.right)
    
        helper(root)
        return self.ans









