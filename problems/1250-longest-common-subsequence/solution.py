class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        # text1 = col
        # text2 = row

        for r in range(len(text2)):
            for c in range(len(text1)):
                if text2[r] == text1[c]:
                    matrix[r + 1][c + 1] = matrix[r][c] + 1
                else:
                    matrix[r + 1][c + 1] = max(matrix[r + 1][c], matrix[r][c + 1])
        
        return matrix[-1][-1]


