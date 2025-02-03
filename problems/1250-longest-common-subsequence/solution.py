class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        # rows = text2, cols = text1

        for r in range(len(text2)):
            for c in range(len(text1)):
                t1Char = text1[c]
                t2Char = text2[r]

                if t1Char == t2Char:
                    matrix[r + 1][c + 1] = matrix[r][c] + 1
                else:
                    matrix[r + 1][c + 1] = max(matrix[r + 1][c], matrix[r][c + 1])
                
        return matrix[-1][-1]


