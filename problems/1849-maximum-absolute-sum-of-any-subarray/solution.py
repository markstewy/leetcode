class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxNegSums = [0]
        maxPosSums = [0]

        totals = []
        total = 0

        for n in nums:
            total += n
            totals.append(total)
            maxNeg = min(maxNegSums[-1], total)
            maxPos = max(maxPosSums[-1], total)
            maxNegSums.append(maxNeg)
            maxPosSums.append(maxPos)

        absMax = 0
        print(totals)
        print(maxNegSums)
        print(maxPosSums)

        for i, t in enumerate(totals):
            absMax = max(absMax, t - maxNegSums[i], abs(t - maxPosSums[i]))
        
        return absMax
