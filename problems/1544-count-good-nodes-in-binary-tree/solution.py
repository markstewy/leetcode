# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0

        def helper(node, prior):
            if not node:
                return
            if node.val >= prior:
                self.goodCount += 1
                prior = node.val

            helper(node.right, prior)
            helper(node.left, prior)
        
        helper(root, -float("infinity"))

        return self.goodCount
