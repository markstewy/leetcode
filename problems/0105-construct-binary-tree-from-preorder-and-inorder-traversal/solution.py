# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderIdx = {}
        for i, n in enumerate(inorder):
            inorderIdx[n] = i

        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return None
                
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)

            partitionIdx = inorderIdx[rootVal]

            root.left = dfs(l, partitionIdx - 1)
            root.right = dfs(partitionIdx + 1, r)

            return root
        
        l = 0
        r = len(preorder) - 1
        return dfs(l, r)
