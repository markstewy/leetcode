# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.helper(0, root)

        return self.ans


    def helper(self, i, node):
        if not node:
            return

        if len(self.ans) - 1 < i:
            self.ans.append([])
        self.ans[i].append(node.val)
        i += 1
        if node.left:
            self.helper(i, node.left)
        if node.right:
            self.helper(i, node.right)

