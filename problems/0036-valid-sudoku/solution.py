class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqs = collections.defaultdict(set)


        for r in range(len(board)):
            for c in range(len(board[0])):
                v = board[r][c]
                
                if v == ".":
                    continue
                
                if v in rows[r] or v in cols[c] or v in sqs[(r//3, c//3)]:
                    return False
                
                rows[r].add(v)
                cols[c].add(v)
                sqs[(r//3, c//3)].add(v)
    
        return True
                
