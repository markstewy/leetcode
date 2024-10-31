class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlap(n1, n2):
            l1, r1 = n1[0], n1[1]
            l2, r2 = n2[0], n2[1]

            if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
                return True
            return False
        
        def combine(n1, n2):
            return [min(n1[0], n2[0]), max(n1[1], n2[1])]

        intervals.sort()
        ans = intervals[0:1]

        for intv in intervals:
            if isOverlap(ans[-1], intv):
                ans[-1] = combine(ans[-1], intv)
            else:
                ans.append(intv)
        return ans
