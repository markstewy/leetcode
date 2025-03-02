class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        stack = deque([[0, 0, 1]])
        directions = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
        visited = set()
        for r in grid:
            print(r)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        while stack:
            r, c, l = stack.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1 and grid[r][c] == 0:
                return l
            
            for nr, nc in directions:
                nr = nr + r
                nc = nc + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append([nr, nc, l + 1])
        
        return -1

            
            



