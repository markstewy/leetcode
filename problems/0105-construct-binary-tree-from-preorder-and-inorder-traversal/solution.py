# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])

        # pass the correct sub arrays in
        # in preorder remove rot by starting from index 1 instead of 0
        # in inorder remove root by not includeing the mid (don't +1 so the subarray doesn't capture it)
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        return root
