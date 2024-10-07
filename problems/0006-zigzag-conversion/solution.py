class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        rowIdx = 0
        lastRowIdx = numRows - 1
        goingDown = True
        rows = [""] * numRows

        for i, c in enumerate(s):
            rows[rowIdx] += c
            if goingDown:
                rowIdx += 1
            else:
                rowIdx -= 1

            if rowIdx == lastRowIdx:
                goingDown = False
            if rowIdx == 0:
                goingDown = True

        ans = ""
        for s in rows:
            ans += s
        
        return ans


