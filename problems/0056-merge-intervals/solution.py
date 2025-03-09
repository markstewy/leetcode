class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        def isOverlap(i1, i2):
            return i1[0] <= i2[0] <= i1[1] or i1[0] <= i2[1] <= i1[1] or i2[0] <= i1[0] <= i2[1] or i2[0] <= i1[1] <= i2[1]
        
        def merge(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        ans = [intervals[0]]

        for i in intervals:
            if isOverlap(i, ans[-1]):
                ans[-1] = merge(ans[-1], i)
            else:
                ans.append(i)
        
        return ans
