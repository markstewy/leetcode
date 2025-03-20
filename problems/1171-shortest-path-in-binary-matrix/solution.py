class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        dq = deque([(0, 0, 1)])
        visited = set()
        directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

        while dq:
            print(dq[0])
            r, c, count = dq.popleft()

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return count

            for nr, nc in directions:
                nr += r
                nc += c

                if (nr, nc) not in visited and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                    visited.add((nr, nc))
                    dq.append((nr, nc, count + 1))
        return -1
            


