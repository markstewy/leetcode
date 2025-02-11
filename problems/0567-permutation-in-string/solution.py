class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        s2count = {}

        matches = 0
        needed = len(s1count.keys())

        l = 0
        for r in range(len(s2)):

            # add new char on right
            c = s2[r]
            s2count[c] = s2count.get(c, 0) + 1

            if c in s1count and s1count[c] == s2count[c]:
                matches += 1
            if c in s1count and s1count[c] == s2count[c] - 1:
                matches -=1
            
            # remove trailing char on left
            if r - l + 1 > len(s1):
                c = s2[l]
                l += 1
                s2count[c] -= 1

                if c in s1count and s1count[c] == s2count[c]:
                    matches += 1
                if c in s1count and s1count[c] == s2count[c] + 1:
                    matches -=1
            if matches == needed:
                return True
        
        return matches == needed

