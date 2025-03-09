class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for r in range(1, numRows + 1):
            # print(r)
            row = []
            for i in range(r):
                if i == 0:
                    row.append(1)
                elif i == r - 1:
                    row.append(1)
                else:
                    row.append(ans[-1][i - 1] + ans[-1][i])
            ans.append(row)
        
        return ans
                



                
            

