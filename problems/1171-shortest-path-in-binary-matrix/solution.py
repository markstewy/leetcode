class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        dq = deque()
        dq.append((0, 0, 1))
        visiting = set()

        dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

        while dq:
            r, c, l = dq.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return l

            for rdir, cdir in dirs:
                nr, nc = r + rdir, c + cdir
                if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                    return l + 1
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visiting and grid[nr][nc] == 0:
                    dq.append((nr, nc, l + 1))
                    visiting.add((nr, nc))
        
        return -1

