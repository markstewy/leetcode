class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        win, count = {}, {}

        # initialize counters
        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
            win[s2[i]] = win.get(s2[i], 0) + 1

        matches = 0
        needed = len(count.keys())

        # initialize matches
        for n, c in count.items():
            if n in win and win[n] == c:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == needed:
                return True
            
            # update l
            c = s2[l]
            win[c] -= 1
            l += 1
            if c in count and count[c] == win[c]:
                matches += 1
            if c in count and count[c] - 1 == win[c]:
                matches -= 1
            
            # update r
            c = s2[r]
            win[c] = win.get(c, 0) + 1
            if c in count and count[c] == win[c]:
                matches += 1
            if c in count and count[c] + 1 == win[c]:
                matches -= 1
            
        return matches == needed
