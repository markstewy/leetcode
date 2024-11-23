# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def helper(root, priorMax):
            if not root:
                return
            if root.val >= priorMax:
                self.good += 1
            
            priorMax = max(root.val, priorMax)

            helper(root.left, priorMax)
            helper(root.right, priorMax)
        
        helper(root, -float("infinity"))
        return self.good
            

