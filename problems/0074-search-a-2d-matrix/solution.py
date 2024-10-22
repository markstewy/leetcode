class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        targetRow = -1

        while l <= r:
            m = l + (r - l) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                targetRow = m
                break
        
        if targetRow == -1:
            return False
        
        l = 0
        r = len(matrix[targetRow]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target > matrix[targetRow][m]:
                l = m + 1
            elif target < matrix[targetRow][m]:
                r = m - 1
            else:
                return True
        return False


