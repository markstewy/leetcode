# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0

        def dfs(root, maxParent):
            if not root:
                return
            if root.val >= maxParent:
                self.goodCount += 1
            
            maxParent = max(root.val, maxParent)
            dfs(root.left, maxParent)
            dfs(root.right, maxParent)
        
        dfs(root, -float("infinity"))
        return self.goodCount

