class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        targetRow = None

        while l <= r:
            m = l + (r - l) // 2

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                targetRow = matrix[m]
                break
        
        if targetRow == None:
            return False
        

        l = 0
        r = len(targetRow) - 1

        while l <= r:
            m = l + (r - l) // 2

            if targetRow[m] < target:
                l = m + 1
            elif targetRow[m] > target:
                r = m - 1
            else:
                return True
        
        return False
            
