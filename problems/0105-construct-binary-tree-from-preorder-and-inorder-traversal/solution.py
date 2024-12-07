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
        
        self.preorderIdx = 0
        l = 0
        r = len(preorder) - 1

        def dfs(l, r):
            if l > r:
                return
            
            rootVal = preorder[self.preorderIdx]
            self.preorderIdx += 1
            partition = inorderIdx[rootVal]

            root = TreeNode(rootVal)
            root.left = dfs(l, partition - 1)
            root.right = dfs(partition + 1, r)

            return root
        
        return dfs(l, r)

    
