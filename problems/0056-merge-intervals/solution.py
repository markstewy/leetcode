# [[1,3],[2,6],[8,10],[15,18]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []    
        intervals.sort(key = lambda i : i[0])

        l = intervals[0][0]
        r = intervals[0][1]

        for s in intervals:
            leftOverlap = s[0] >= l and s[0] <= r
            rightOverlap = s[1] >= l and s[1] <= r
            fullOverlap = s[0] <= l and s[1] >= r
            if leftOverlap or rightOverlap or fullOverlap:
                l = min(s[0], l)
                r = max(s[1], r)
            else:
                ans.append([l, r])
                l = s[0]
                r = s[1]
        
        ans.append([l, r])
        return ans
            
        
            



        
            

