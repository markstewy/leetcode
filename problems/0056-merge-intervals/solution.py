class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        def isOverlap(int1, int2):
            b1, e1, = int1[0], int1[1]
            b2, e2, = int2[0], int2[1]
            return b1 <= b2 <= e1 or b1 <= e2 <= e1 or b2 <= b1 <= e2 or b2 <= e1 <= e2

        def merge(int1, int2):
            return [min(int1[0], int2[0]), max(int1[1], int2[1])]

        
        ans = [intervals[0]]
        for i in intervals:
            if isOverlap(i, ans[-1]):
                ans[-1] = merge(i, ans[-1])
            else:
                ans.append(i)
        
        return ans

