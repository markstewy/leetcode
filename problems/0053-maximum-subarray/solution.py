class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNegSum = [0]
        totals = []
        total = 0

        for n in nums:
            total += n
            totals.append(total)
            maxNegSum.append(min(maxNegSum[-1], total))
        
        print()
        print(maxNegSum)

        maxSub = nums[0]
        for i, n in enumerate(totals):
            maxSub = max(maxSub, n - maxNegSum[i])
        
        return maxSub


            


        
        
