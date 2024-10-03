class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False    
    
        s1Count, s2Count = {}, {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        needed = len(s1Count)
        matches = 0

        for c in s1Count:
            if c in s2Count and s2Count[c] == s1Count[c]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == needed:
                return True
            
            # add r
            c = s2[r]
            s2Count[c] = s2Count.get(c, 0) + 1
            if c in s1Count and s2Count[c] == s1Count[c]:
                matches += 1
            if c in s1Count and s2Count[c] == s1Count[c] + 1:
                matches -= 1

            # remove l
            c = s2[l]
            s2Count[c] -= 1
            if c in s1Count and s2Count[c] == s1Count[c]:
                matches += 1
            if c in s1Count and s2Count[c] == s1Count[c] - 1:
                matches -= 1
            l += 1
        
        return matches == needed

