class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        def isOverlap(int1, int2):
            l1, r1 = int1[0], int1[1]
            l2, r2 = int2[0], int2[1]

            if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
                return True
            else:
                return False
            
        def combine(int1, int2):
            return [min(int1[0], int2[0]), max(int1[1], int2[1])]
        
        ans = intervals[0:1]

        for i in intervals:
            if isOverlap(i, ans[-1]):
                ans[-1] = combine(i, ans[-1])
            else:
                ans.append(i)
        
        return ans
