# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # go through each preorder 1 by 1
        # lookup partition in inorder

        self.preIdx = 0
        inOrderIdx = {}
        for i, v in enumerate(inorder):
            inOrderIdx[v] = i
        
        def dfs(l, r):
            if l > r:
                return None
            
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)
            m = inOrderIdx[rootVal]

            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)

