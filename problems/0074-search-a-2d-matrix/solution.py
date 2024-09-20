class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow, rrow = 0, len(matrix) - 1
        while lrow <= rrow:
            mrow = lrow + (rrow - lrow) // 2

            if target < matrix[mrow][0]:
                rrow = mrow - 1
            elif target > matrix[mrow][-1]:
                lrow = mrow + 1
            else:
                row = matrix[mrow]
                l, r = 0, len(row) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if target > row[m]:
                        l = m + 1
                    elif target < row[m]:
                        r = m - 1
                    else:
                        break
                return row[m] == target

