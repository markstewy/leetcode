class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        
        def delIsland(r, c):
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            if r > 0:
                delIsland(r - 1, c)
            if r < len(grid) - 1:
                delIsland(r + 1, c)
            if c > 0:
                delIsland(r, c - 1)
            if c < len(grid[0]) - 1:
                delIsland(r, c + 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islandCount += 1
                    delIsland(r, c)
        
        return islandCount

