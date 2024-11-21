# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []

        def helper(root, level):
            if not root:
                return
            if len(self.levels) - 1 < level:
                self.levels.append([])
            self.levels[level].append(root.val)
        
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root, 0)

        return self.levels
