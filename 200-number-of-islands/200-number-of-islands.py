class Solution:        
    def numIslands(self, grid: List[List[str]]) -> int:
        xMaxIdx = len(grid[0]) - 1
        yMaxIdx = len(grid) - 1
        
        def isLand(x, y):
            # out of bounds
            if x < 0 or x > xMaxIdx or y < 0 or y > yMaxIdx:
                return False
            if grid[y][x] == '1':
                return True
            else:
                return False
    
        def deleteIsland(x, y):
            # don't over out of bounds, recursive delete all adjacent land '1'
            if isLand(x, y):
                grid[y][x] = '0'
                deleteIsland(x + 1, y)
                deleteIsland(x - 1, y)
                deleteIsland(x, y + 1)
                deleteIsland(x, y - 1)
                
        
        counter = 0
        # if there is an island, increment the counter and then delete the island
        for (iy, y) in enumerate(grid):
            print(iy)
            for (ix, x) in enumerate(grid[iy]):
                if grid[iy][ix] == '1':
                    counter = counter + 1
                    deleteIsland(ix, iy)
        return counter