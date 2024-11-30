class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def isOverlap(n1, n2):
            l1, r1 = n1[0], n1[1]
            l2, r2 = n2[0], n2[1]

            if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
                return True
            return False

        def merge(n1, n2):
            return [min(n1[0], n2[0]), max(n1[1], n2[1])]

        intervals.sort()
        merged = [intervals[0]]

        for i in intervals:
            if isOverlap(i, merged[-1]):
                merged[-1] = merge(i, merged[-1])
            else:
                merged.append(i)
        
        return merged
