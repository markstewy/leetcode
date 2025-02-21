# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.valSet = set()
        
        def helper(root):
            if not root:
                return
            
            self.valSet.add(root.val)
            
            if root.left:
                root.left.val = root.val * 2 + 1
                helper(root.left)
            if root.right:
                root.right.val = root.val * 2 + 2
                helper(root.right)
        
        helper(self.root)
            

    def find(self, target: int) -> bool:
        return target in self.valSet
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
