# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0

        def helper(root, mxParent):
            if not root:
                return
            if root.val >= mxParent:
                self.goodCount += 1
            
            mxParent = max(mxParent, root.val)
            helper(root.left, mxParent)
            helper(root.right, mxParent)
        
        helper(root, -float("infinity"))

        return self.goodCount
