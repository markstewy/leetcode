class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        count = {}

        l = 0
        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1

            if r - l + 1 > k:
                c = s[l]
                count[c] -= 1
                if count[c] == 0:
                    del count[c]
                l += 1
            if r - l + 1 == k:
                lborder = s[l - 1] if l > 0 else None
                rborder = s[r + 1] if r < len(s) - 1 else None
    
                if len(count.keys()) == 1 and lborder != s[r] and rborder != s[r]:
                    return True

        return len(count.keys()) == 1 and lborder != s[r] and rborder != s[r]
