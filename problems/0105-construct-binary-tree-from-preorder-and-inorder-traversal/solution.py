# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # move through preorder 1 by 1
        # lookup inorder partition
        inorderIdxs = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
        
            rootval = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(rootval)
            m = inorderIdxs[rootval]
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)
            
            return root

        return dfs(0, len(preorder) - 1)
