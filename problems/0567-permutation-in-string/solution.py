class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1, s2 = s1.lower(), s2.lower()
        s1Count, s2WinCount = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2WinCount[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(len(s1Count)):
            if s1Count[i] == s2WinCount[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
        
            # remove l from count (adj matches)
            letter_index = ord(s2[l]) - ord("a")
            s2WinCount[letter_index] -= 1
            if s2WinCount[letter_index] == s1Count[letter_index]:
                matches += 1
            if s2WinCount[letter_index] + 1 == s1Count[letter_index]:
                matches -= 1
            l += 1

            # add r to count (adj matches)
            letter_index = ord(s2[r]) - ord("a")
            s2WinCount[letter_index] += 1
            if s2WinCount[letter_index] == s1Count[letter_index]:
                matches += 1
            if s2WinCount[letter_index] == s1Count[letter_index] + 1:
                matches -= 1
            
        return matches == 26


