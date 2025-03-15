class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        totals = []
        total = 0
        for n in nums:
            total += n
            totals.append(total)
        
        prevNeg = [0]
        prevPos = [0]

        for t in totals:
            minNeg = min(prevNeg[-1], t)
            maxPos = max(prevPos[-1], t)
            prevNeg.append(minNeg)
            prevPos.append(maxPos)
        
        absSum = abs(nums[0])

        for i, t in enumerate(totals):
            absSum = max(absSum, abs(t - prevPos[i]), abs(t - prevNeg[i]))
        
        return absSum

