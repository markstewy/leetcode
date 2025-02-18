class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        targetRow = None

        while l <= r:
            m = l + (r - l) // 2

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                targetRow = m
                break
        if targetRow == None:
            return False

        vals = matrix[targetRow]
        l = 0
        r = len(vals) - 1

        while l <= r:
            m = l + (r - l) // 2
            if vals[m] < target:
                l = m + 1
            elif vals[m] > target:
                r = m - 1
            else:
                return True
        
        return False

