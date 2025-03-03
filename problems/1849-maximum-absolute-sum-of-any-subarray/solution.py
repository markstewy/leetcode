class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        totals = []
        prevPosSum = [0]
        prevNegSum = [0]

        total = 0
        maxSum = 0
        minSum = 0

        for n in nums:
            total += n
            maxSum = max(maxSum, total)
            minSum = min(minSum, total)

            totals.append(total)
            prevPosSum.append(maxSum)
            prevNegSum.append(minSum)
        
        maxAbsSum = abs(nums[0])

        for i in range(len(nums)):
            posMax = totals[i] - prevNegSum[i] # minus a negative
            negMax = totals[i] - prevPosSum[i] # minus a positive 
            maxAbsSum = max(maxAbsSum, abs(posMax), abs(negMax))
        
        return maxAbsSum


