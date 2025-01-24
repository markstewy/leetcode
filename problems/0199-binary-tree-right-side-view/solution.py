# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightside = []
        
        def traversal(root, level):
            if not root:
                return
            if len(self.rightside) < level:
                self.rightside.append(root.val)
            traversal(root.right, level + 1)
            traversal(root.left, level + 1)

        traversal(root, 1)
        return self.rightside
