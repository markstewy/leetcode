class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # track duplicates in row, col and squares with a set each

        rows = collections.defaultdict(set) # key = row number
        cols = collections.defaultdict(set) # key = col number
        sqs = collections.defaultdict(set) # key = tuple of integer math ie. (row//3, col//3)  >>> rows 1-2 // 3 = 1, 3-5 // 3 = 1

        for r in range(9):
            for c in range(9):
                v = board[r][c]

                if v == ".":
                    continue
                
                # check if duplicate exists, if so fail <return False>
                if (
                    v in rows[r]
                    or v in cols[c]
                    or v in sqs[(r//3, c//3)]
                ):
                    return False
                
                rows[r].add(v)
                cols[c].add(v)
                sqs[(r//3, c//3)].add(v)
        
        return True

