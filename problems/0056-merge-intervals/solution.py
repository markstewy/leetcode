class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        def isOverlap(i1, i2):
            s1, e1 = i1[0], i1[1]
            s2, e2 = i2[0], i2[1]
            return s1 <= s2 <= e1 or s1 <= e2 <= e1 or s2 <= s1 <= e2 or s2 <= e1 <= e2
            
        def merge(i1, i2):
            s = min(i1[0], i2[0])
            e = max(i1[1], i2[1])
            return [s, e]
        
        for i in intervals:
            if isOverlap(ans[-1], i):
                ans[-1] = merge(ans[-1], i)
            else:
                ans.append(i)
        
        return ans
            

