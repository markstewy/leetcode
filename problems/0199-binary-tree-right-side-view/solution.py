# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightView = []
        
        # do aright traversal that tracks level
        def helper(node, level):
            if node == None:
                return
            if len(self.rightView) - 1 < level:
                self.rightView.append(node.val)

            helper(node.right, level + 1)
            helper(node.left, level + 1)
        
        helper(root, 0)
        return self.rightView

