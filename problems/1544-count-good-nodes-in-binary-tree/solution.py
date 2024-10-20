# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0

        def helper(node, priorMax):
            if not node:
                return

            if node.val >= priorMax:
                self.goodCount += 1
            helper(node.left, max(priorMax, node.val))
            helper(node.right, max(priorMax, node.val))
        
        helper(root, root.val)
        return self.goodCount

