class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
            if numRows == 0:
                return []
            
            matrix = [[1]]

            for r in range(1, numRows):
                childRow = [0] * (r + 1)
                matrix.append(childRow)
                parentRow = matrix[r - 1]
                for i in range(len(childRow)):
                    l = parentRow[i - 1] if i > 0 else 0
                    r = parentRow[i] if i < len(parentRow) else 0
                    childRow[i] = l + r
            
            return matrix


           



