class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        targetRow = -1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                targetRow = m
                break
        
        if targetRow == -1:
            return False
        
        l = 0
        values = matrix[targetRow]
        r = len(values)

        while l <= r:
            m = l + (r - l) // 2

            if values[m] > target:
                r = m - 1
            elif values[m] < target:
                l = m + 1
            else:
                return True
        
        return False


