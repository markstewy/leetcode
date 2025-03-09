class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevMins = [0]
        totals = []

        total = 0
        prevMin = 0


        for n in nums:
            total += n
            totals.append(total)
            prevMin = min(prevMin, total)
            prevMins.append(prevMin)

        maxSum = totals[0]
        for i in range(len(totals)):
            summ = totals[i] - prevMins[i]
            maxSum = max(maxSum, summ)
        
        return maxSum

