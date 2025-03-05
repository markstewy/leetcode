class Solution:
    def coloredCells(self, n: int) -> int:
        return n**2 + (n-1)**2 # my final solution! proud of it...

        # if n == 1:
        #     return 1

        # offset = False
        # total = 0

        # for _ in range(n * 2 - 1):
        #     if offset:
        #         total += n - 1
        #     else:
        #         total += n
        #     offset = not offset
        
        # return total
            



