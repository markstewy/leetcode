class Solution:
    def partitionString(self, s: str) -> int:
        cSet = set()

        numSubs = 1
        for c in s:
            if c in cSet:
                numSubs += 1
                cSet.clear()
            
            cSet.add(c)
        
        return numSubs

