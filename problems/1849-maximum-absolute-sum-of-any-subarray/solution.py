class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prevMins = [0]
        prevMaxs = [0]
        totals = []

        total = 0
        prevMin = 0
        prevMax = 0

        for n in nums:
            total += n
            prevMin = min(prevMin, total)
            prevMax = max(prevMax, total)

            totals.append(total)
            prevMins.append(prevMin)
            prevMaxs.append(prevMax)
        
        absMaxSum = abs(totals[0])

        for i, n in enumerate(totals):
            maxNeg = n - prevMaxs[i]
            maxPos = n - prevMins[i]

            absMaxSum = max(abs(maxNeg), abs(maxPos), absMaxSum)
        
        return absMaxSum



