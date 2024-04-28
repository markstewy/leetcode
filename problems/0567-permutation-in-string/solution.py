class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Count = {} # a char counf of the entire s1 string
        s2Count = {} # a char count of the sub array within s2

        # initialize counts
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1
        
        matches = 0
        need = len(s1Count) # matches for every char in s1

        # initialize matches count
        for c in s2Count.keys():
            if c in s1Count and s2Count[c] == s1Count[c]:
                matches += 1

        # sliding window of length s1: add r and remove l then update matches
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == need:
                return True
                
            # add r and update matches
            rc = s2[r]
            s2Count[rc] = s2Count.get(rc, 0 ) + 1
            if rc in s1Count and s2Count[rc] == s1Count[rc]:
                matches += 1
            if rc in s1Count and s2Count[rc] == s1Count[rc] + 1:
                matches -= 1 # one too many, no longer a match

            # remove l and update matches
            lc = s2[l]
            s2Count[lc] -= 1
            if lc in s1Count and s2Count[lc] == s1Count[lc]:
                matches += 1
            if lc in s1Count and s2Count[lc] == s1Count[lc] - 1:
                matches -= 1 # one too few, no longer a match
            l += 1
            
        return matches == need

