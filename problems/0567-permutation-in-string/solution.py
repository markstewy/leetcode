class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = {}

        needed = len(count1)
        matches = 0

        l = 0
        for r in range(len(s2)):
            if matches == needed:
                return True

            c = s2[r]
            count2[c] = count2.get(c, 0) + 1

            if c in count1 and count1[c] == count2[c]:
                matches += 1
            
            if r - l + 1 > len(s1):
                c = s2[l]
                count2[c] -= 1
                
                if c in count1 and count1[c] == count2[c] + 1:
                    matches -= 1
                l += 1
        
        return matches == needed
