class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        dq = deque()
        dq.append([0, 0, 1])
        directions = [(1, 1), (1, 0), (1, -1), (0,1), (0,-1), (-1,1),(-1,0),(-1,-1)]
        visited = set()

        while dq:
            r, c, l = dq.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return l

            for nr, nc in directions:
                nr += r
                nc += c

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dq.append([nr, nc, l + 1])
        return -1
