# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # go through preorder 1 by 1 and assign left and right
        # find partition in inorder
        # while l < r

        self.preIdx = 0
        inorderIdx = {}
        for i, v in enumerate(inorder):
            inorderIdx[v] = i
        

        def dfs(l, r):
            if l > r:
                return None

            rootval = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootval)

            partition = inorderIdx[rootval]
            root.left = dfs(l, partition - 1)
            root.right = dfs(partition + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)

