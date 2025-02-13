# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        
        def helper(root, mx):
            if not root:
                return
            if root.val >= mx:
                self.good += 1
            mx = max(mx, root.val)

            helper(root.left, mx)
            helper(root.right, mx)
    
        helper(root, -float("infinity"))
        return self.good

