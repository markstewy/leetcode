class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        # row = text1
        # col = text2

        for r in range(len(text2)):
            for c in range(len(text1)):
                if text1[c] == text2[r]:
                    matrix[r+1][c+1] = matrix[r][c] + 1
                else:
                    matrix[r+1][c+1] = max(matrix[r][c], matrix[r+1][c], matrix[r][c+1])


        return matrix[-1][-1]
