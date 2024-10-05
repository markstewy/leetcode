class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for r, ch1 in enumerate(text1):
            for c, ch2 in enumerate(text2):
                if ch1 == ch2:
                    dp[r + 1][c + 1] = 1 + dp[r][c]
                else:
                    dp[r + 1][c + 1] = max(dp[r][c + 1], dp[r + 1][c])
        return dp[-1][-1]
