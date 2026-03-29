class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for i, c in enumerate(pattern):
            if c not in words:
                if s[i] in words.values():
                    return False
                words[c] = s[i]
            elif words[c] != s[i]:
                return False
        return True
