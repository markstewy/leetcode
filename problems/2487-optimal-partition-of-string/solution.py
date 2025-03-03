class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        cset = set()

        for i in range(len(s)):
            if s[i] in cset:
                count += 1
                cset.clear()
            cset.add(s[i])
        
        return count


