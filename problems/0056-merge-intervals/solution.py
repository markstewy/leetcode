class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        ans.append(intervals[0])
                
        def isOverlap(t1, t2):
            if (
                t2[0] <= t1[0] <= t2[1] or
                t2[0] <= t1[1] <= t2[1] or
                t1[0] <= t2[0] <= t1[1] or
                t1[0] <= t2[1] <= t1[1]
                ):
                return True
            else:
                return False
            
        
        def merge(t1, t2):
            return [min(t1[0], t2[0]), max(t1[1], t2[1])]
            
        for curr in intervals:
            if isOverlap(ans[-1], curr):
                ans[-1] = merge(ans[-1], curr)
            else:
                ans.append(curr)
        return ans





