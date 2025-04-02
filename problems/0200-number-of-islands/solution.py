class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        
        def helper(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return
            if (r, c) in visited:
                return
            
            visited.add((r, c))

            for nr, nc in directions:
                nr += r
                nc += c

                helper(nr, nc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    helper(r, c)
        
        return count


