class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [] total
        # [] running lowest total
        minTotals = [0]
        minTotal = 0

        totals = []
        total = 0

        for n in nums:
            total += n
            totals.append(total)

            minTotal = min(minTotal, total)
            minTotals.append(minTotal)

        maxSum = nums[0]
        for i in range(len(totals)):
            currMaxSum = totals[i] - minTotals[i]
            maxSum = max(maxSum, currMaxSum)
        
        return maxSum




        print(totals)
        print(minTotals)

        # total[i] - runninglowesttotal[i] = max for this index


