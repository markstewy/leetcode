class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # col text1 row text2
        matrix = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for r in range(len(text2)):
            for c in range(len(text1)):
                char1 = text1[c]
                char2 = text2[r]

                if char1 == char2:
                    matrix[r + 1][c + 1] = matrix[r][c] + 1
                else:
                    matrix[r + 1][c + 1] = max(matrix[r + 1][c], matrix[r][c + 1])
    
        return matrix[-1][-1]


