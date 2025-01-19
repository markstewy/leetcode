class Solution:
    def partitionString(self, s: str) -> int:
        cset = set()
        count = 1
        
        for c in s:
            if c in cset:
                cset.clear()
                count += 1
            cset.add(c)
        
        return count
