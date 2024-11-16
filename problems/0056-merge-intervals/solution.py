class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        def isOverlap(interval1, interval2):
            l1, r1 = interval1[0], interval1[1]
            l2, r2 = interval2[0], interval2[1]

            if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= l1 <= r2:
                return True
            return False
        
        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        
        ans = []
        ans.append(intervals[0])

        for i in intervals:
            if isOverlap(i, ans[-1]):
                ans[-1] = merge(ans[-1], i)
            else:
                ans.append(i)
        
        return ans

