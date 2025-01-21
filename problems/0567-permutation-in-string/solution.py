class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = {}

        matches = 0
        needed = len(s1Count.keys())

        l = 0
        for r in range(len(s2)):
            c = s2[r]
            s2Count[c] = s2Count.get(c, 0) + 1

            if c in s1Count and s1Count[c] == s2Count[c]:
                matches += 1
            if c in s1Count and s1Count[c] == s2Count[c] - 1:
                matches -= 1
            
            while r - l + 1 > len(s1):
                c = s2[l]
                s2Count[c] -= 1
                l += 1

                if c in s1Count and s1Count[c] == s2Count[c]:
                    matches += 1
                if c in s1Count and s1Count[c] == s2Count[c] + 1:
                    matches -= 1

            if matches == needed:
                return True
        
        return matches == needed
