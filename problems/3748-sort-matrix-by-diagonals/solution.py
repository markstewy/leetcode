class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        self.grid = grid
        height = len(grid)
        width = len(grid[0])

        def sortDiag(startr, startc, desc: bool):
            diag = []
            r = startr
            c = startc
            while r < height and c < width:
                diag.append(self.grid[r][c])
                r += 1
                c += 1
            # print(f"diag: {diag}")
            diag.sort(reverse=desc)
            # print(f"diag: {diag}")
            r = startr
            c = startc
            while r < height and c < width:
                self.grid[r][c] = diag.pop()
                # print(self.grid[r][c])
                r += 1
                c += 1

        for r in range(height):
            sortDiag(r, 0, False)
        for c in range(1, width):
            sortDiag(0, c, True)

        return grid
      
