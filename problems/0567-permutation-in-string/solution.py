class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = {}, {}

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        matches = 0
        needed = len(s1Count.keys())

        l = 0
        for r in range(len(s2)):
            # add r
            c = s2[r]
            s2Count[c] = s2Count.get(c, 0) + 1
            if c in s1Count and s2Count[c] == s1Count[c]:
                matches += 1
            if c in s1Count and s2Count[c] == s1Count[c] + 1:
                matches -= 1 # one too many

            # if len of string is 1 too long then bring up l
            if (r - l + 1) > len(s1):
                c = s2[l]
                s2Count[c] -= 1
                if c in s1Count and s2Count[c] == s1Count[c]:
                    matches += 1
                if c in s1Count and s2Count[c] == s1Count[c] - 1:
                    matches -= 1 # one too few
                l += 1

            # if matches are exact return true
            if matches == needed:
                return True
        
        return False





