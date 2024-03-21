class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue

                if (
                    v in rows[r]
                    or v in cols[c]
                    or v in sqs[(r // 3, c // 3)]
                ):
                    return False

                cols[c].add(v)
                rows[r].add(v)
                sqs[(r//3, c//3)].add(v)
        return True

    
