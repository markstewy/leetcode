# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []

        def helper(root, l):
            if not root:
                return
            if l > len(self.levels) - 1:
                self.levels.append([])
            self.levels[l].append(root.val)
            if root.left:
                helper(root.left, l + 1)
            if root.right:
                helper(root.right, l + 1)
        
        helper(root, 0)
        return self.levels

