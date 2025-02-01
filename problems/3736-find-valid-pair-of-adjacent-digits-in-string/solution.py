class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)

        for i in range(1, len(s)):
            if s[i] != s[i - 1] and count[s[i]] == int(s[i]) and count[s[i - 1]] == int(s[i - 1]):
                ans = s[i - 1] + s[i]
                return ans

        return ""
            
            
