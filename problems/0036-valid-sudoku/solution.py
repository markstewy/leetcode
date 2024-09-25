class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                n = board[r][c]

                if n == ".":
                    continue
                
                if (n in rows[r] or n in cols[c] or n in sqs[(r//3, c//3)]):
                    return False
                
                rows[r].add(n)
                cols[c].add(n)
                sqs[(r//3, c//3)].add(n)
            
        return True

