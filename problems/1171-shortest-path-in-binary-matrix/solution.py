class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        dq = deque([(0, 0, 1)])
        directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        visited = set((0, 0))

        def isValid(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return False
            if (r, c) in visited:
                return False
            if grid[r][c] != 0:
                return False
            return True
        
        while dq:
            r, c, count = dq.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return count

            for nr, nc in directions:
                nr += r
                nc += c

                if isValid(nr, nc):
                    dq.append((nr, nc, count + 1))
                    visited.add((nr, nc))
        
        return -1

            
