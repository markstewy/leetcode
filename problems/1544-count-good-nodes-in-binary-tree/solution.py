# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodeCount = 0
        
        def helper(root, maxval):
            if not root:
                return
            if root.val >= maxval: # valid node is greater than ancestors
                self.goodNodeCount += 1
                helper(root.left, root.val)
                helper(root.right, root.val)
            else:
                helper(root.left, maxval)
                helper(root.right, maxval)
        
        helper(root, -float("infinity"))
        return self.goodNodeCount

