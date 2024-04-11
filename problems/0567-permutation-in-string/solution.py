class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # sliding window of fixed length
        # the window should have exactly same number of each char, no more no less

        s1Count = {}
        window = {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        # track if we have all chars satisfied with "matches"
        # a match is when a char has no more, no less than the char count in s1Count
        matches = 0
        need = len(s1Count)

        # initialize matches
        for c, count in window.items():
            if c not in s1Count:
                continue
            if window[c] == s1Count[c]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == need:
                return True
            
            window[s2[r]] = window.get(s2[r], 0) + 1
            if s2[r] in s1Count and window[s2[r]] == s1Count[s2[r]]:
                matches += 1
            if s2[r] in s1Count and window[s2[r]] == s1Count[s2[r]] + 1:
                matches -= 1

            window[s2[l]] -= 1
            if s2[l] in s1Count and window[s2[l]] == s1Count[s2[l]]:
                matches += 1
            if s2[l] in s1Count and window[s2[l]] == s1Count[s2[l]] - 1:
                matches -= 1
            l += 1
        
        return matches == need


