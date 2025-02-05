class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tree = []
        for i in range(1, numRows + 1):
            tree.append([1] * i)
        
        for r in range(len(tree)):
            for c in range(len(tree[r])):
                if r == 0:
                    tree[r][0] = 1
                    continue
                if c == 0:
                    tree[r][c] = tree[r - 1][0]
                elif c == len(tree[r]) - 1:
                    tree[r][c] = tree[r - 1][-1]
                else:
                    tree[r][c] = tree[r - 1][c] + tree[r - 1][c - 1]
        
        return tree
                
            

                



