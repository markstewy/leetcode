class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.islandSize = 0

        def helper(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if (r, c) in visited or grid[r][c] == 0:
                return
            
            self.islandSize += 1
            self.maxArea = max(self.maxArea, self.islandSize)
            visited.add((r, c))
            
            for nr, nc in directions:
                nr += r
                nc += c
                helper(nr, nc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                helper(r, c)
                self.islandSize = 0
        
        return self.maxArea
                
