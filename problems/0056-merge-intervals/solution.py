class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        def isOverlap(n1, n2):
            l1, r1 = n1[0], n1[1]
            l2, r2 = n2[0], n2[1]

            if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
                return True
            else:
                return False
        
        def combine(n1, n2):
            return [min(n1[0], n2[0]), max(n1[1], n2[1])]
        
        merged = []
    
        for i in intervals:
            if merged and isOverlap(i, merged[-1]):
                merged[-1] = combine(i, merged[-1])
            else:
                merged.append(i)
        
        return merged
