class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.currCount = 0
        visited = set()
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

        def helper(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1 and (r, c) not in visited:
                self.currCount += 1
                self.maxArea = max(self.maxArea, self.currCount)
                visited.add((r, c))
                
                for nr, nc in directions:
                    nr += r
                    nc += c
                    helper(nr, nc)
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    helper(r, c)
                    self.currCount = 0
        
        return self.maxArea
                    

