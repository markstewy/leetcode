class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]


        while len(ans) < numRows:
            ans.append([0] * (len(ans[-1]) + 1))

            currRow = ans[-1]
            priorRow = ans[-2]
            currRow[0] = priorRow[0]
            currRow[-1] = priorRow[-1]

            for i in range(1, len(currRow) - 1):
                currRow[i] = priorRow[i] + priorRow[i - 1]

        return ans            

