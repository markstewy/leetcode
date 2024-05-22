class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {}
        win = {}

        # initialize s1 count and s2 sliding window
        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
            win[s2[i]] = win.get(s2[i], 0) + 1
        
        # initialize matches between s1 and s2 window
        matches = 0
        needed = len(count.keys())

        for s1c, s1count in count.items():
            if s1c in win and win[s1c] == s1count:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            # if matches correct return true
            if matches == needed:
                return True

            # remove l, update matches
            c = s2[l]
            win[c] -= 1
            l += 1
            if c in count and win[c] == count[c]:
                matches += 1
            if c in count and win[c] + 1 == count[c]:
                matches -= 1

            # add r, update matches
            c = s2[r]
            win[c] = win.get(c, 0) + 1
            if c in count and win[c] == count[c]:
                matches += 1
            if c in count and win[c] - 1 == count[c]:
                matches -= 1


        return matches == needed


