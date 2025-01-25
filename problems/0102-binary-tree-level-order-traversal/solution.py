# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.lot = []

        def helper(root, level):
            if not root:
                return

            if level > len(self.lot):
                self.lot.append([])
            self.lot[level - 1].append(root.val)

            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root, 1)
        return self.lot
