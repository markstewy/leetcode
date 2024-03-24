class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if (
                    v in rows[r]
                    or v in cols[c]
                    or v in squares[(r//3, c//3)]
                ):
                    return False

                rows[r].add(v)
                cols[c].add(v)
                squares[(r//3, c//3)].add(v)
            
        return True




