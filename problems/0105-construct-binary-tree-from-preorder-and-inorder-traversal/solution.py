# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # go through preorder one by one
        # find the parition in inorder

        inOrderIdx = {}
        for i, v in enumerate(inorder):
            inOrderIdx[v] = i
        
        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return None
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)
            partition = inOrderIdx[rootVal]
            
            root.left = dfs(l, partition - 1)
            root.right = dfs(partition + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)


        
