class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        count = 0

        def removeIsland(r, c):
            if r >= len(self.grid) or r < 0:
                return
            if c >= len(self.grid[0]) or c < 0:
                return
            if self.grid[r][c] == "1":
                self.grid[r][c] = "0"
                removeIsland(r + 1, c)
                removeIsland(r - 1, c)
                removeIsland(r, c + 1)
                removeIsland(r, c - 1)
            else:
                return
        
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == "1":
                    count += 1
                    removeIsland(r, c)
    
        return count

