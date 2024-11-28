class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count, s2count = {}, {}
        for c in s1:
            s1count[c] = s1count.get(c, 0) + 1
        
        matches = 0
        needed = len(s1count.keys())

        print(s1count)

        l = 0
        for r in range(len(s2)):
            if matches == needed:
                return True

            c = s2[r]
            s2count[c] = s2count.get(c, 0) + 1

            if c in s1count and s2count[c] == s1count[c]:
                matches += 1
            if c in s1count and s2count[c] == s1count[c] + 1:
                matches -= 1
        
            if r - l + 1 > len(s1):
                c = s2[l]
                s2count[c] -= 1

                if c in s1count and s2count[c] == s1count[c]:
                    matches += 1
                if c in s1count and s2count[c] == s1count[c] - 1:
                    matches -= 1
                l += 1
        
        return matches == needed
