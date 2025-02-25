# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = collections.defaultdict(list)

        def helper(root, col, row):
            if not root:
                return

            cols[col].append([col, row, root.val])
            
            helper(root.left, col - 1, row + 1)
            helper(root.right, col + 1, row + 1)
        
        helper(root, 0, 0)
        
        print(cols)
        colNumbers = [col for col in cols.keys()]
        colNumbers.sort()

        ans = []
        for c in colNumbers:
            cols[c].sort(key=lambda x : (x[0], x[1]))
            ans.append([n[2] for n in cols[c]])
        return ans





