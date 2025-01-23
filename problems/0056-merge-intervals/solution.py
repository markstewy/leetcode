class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals:
            return []

        ans = [intervals[0]]
        for interval in intervals:
            if self.isOverlap(interval, ans[-1]):
                ans[-1] = self.mergeInts(interval, ans[-1])
            else:
                ans.append(interval)

        return ans

    def mergeInts(self, int1, int2):
        return [min(int1[0], int2[0]), max(int1[1], int2[1])]

    def isOverlap(self, int1, int2) -> bool:
        l1, r1, l2, r2 = int1[0], int1[1], int2[0], int2[1]

        if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
            return True
        else:
            return False
