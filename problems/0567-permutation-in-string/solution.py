class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1count, s2count = {}, {}

        for i in range(len(s1)):
            s1count[s1[i]] = s1count.get(s1[i], 0) + 1
            s2count[s2[i]] = s2count.get(s2[i], 0) + 1
        
        matches = 0
        needed = len(s1count)

        for n, c in s1count.items():
            if n in s2count and s2count[n] == c:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == needed:
                return True
            # add right
            c = s2[r]
            s2count[c] = s2count.get(c, 0) + 1

            if c in s1count and s2count[c] == s1count[c]:
                matches += 1
            if c in s1count and s2count[c] == s1count[c] + 1:
                matches -= 1
            
            # remove left
            c = s2[l]
            l += 1
            s2count[c] -= 1

            if c in s1count and s2count[c] == s1count[c]:
                matches += 1
            if c in s1count and s2count[c] == s1count[c] - 1:
                matches -= 1
        
        return matches == needed
         
