class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {} # c => count
        window = {}

        # initialize s1Count so we can use it for comparision to window
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        # initizlize window and matches count
        matches = 0
        needed = len(s1Count)
        for i in range(len(s1)):
            c = s2[i]
            window[c] = window.get(c, 0) + 1
            
            if c in s1Count and s1Count[c] == window[c]:
                matches += 1
            if c in s1Count and s1Count[c] + 1 == window[c]:
                matches -= 1


        l = 0 
        for r in range(len(s1), len(s2)):
            if matches == needed:
                return True
            
            # update r and matches
            rc = s2[r]
            window[rc] = window.get(rc, 0) + 1
            if rc in s1Count and s1Count[rc] == window[rc]:
                matches += 1
            if rc in s1Count and s1Count[rc] + 1 == window[rc]:
                matches -= 1

            # update l and matches
            lc = s2[l]
            window[lc] -= 1
            if lc in s1Count and s1Count[lc] == window[lc]:
                matches += 1
            if lc in s1Count and s1Count[lc] - 1 == window[lc]:
                matches -= 1
            l += 1
        
        return matches == needed
