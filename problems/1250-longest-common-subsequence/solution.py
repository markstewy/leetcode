class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for r, ch1 in enumerate(text1):
            for c, ch2 in enumerate(text2):
                if ch1 == ch2:
                    matrix[r + 1][c + 1] = 1 + matrix[r][c]
                else:
                    matrix[r + 1][c + 1] = max(matrix[r][c + 1], matrix[r + 1][c])
        return matrix[-1][-1]


# add extra zero to beginning of each row/col
# if row char == col char then diagonally equals increment current by 1
# else diagonally equals max of values to right or down

#       | u   b   m   r   a   p   g
#     --|------------------------------
#     e | 0   0   0   0   0   0   0   0
#     z | 0   0   0   0   0   0   0   0
#     u | 0   0   0   0   0   0   0   0
#     p | 0   1   1   1   1   1   1   1
#     k | 0   1   1   1   1   1   2   2
#     r | 0   1   1   1   1   1   2   2
#       | 0   1   1   1   2   2   2   2


# answer is "ur" or 2
