# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels = []

        def dfs(root, l):
            if not root:
                return
            if l > len(self.levels):
                self.levels.append(root.val)

            dfs(root.right, l + 1)
            dfs(root.left, l + 1)
        
        dfs(root, 1)
        return self.levels

