class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        totals = []
        for n in nums:
            total += n
            totals.append(total)
        
        prevMins = [0]
        for t in totals:
            currMin = min(prevMins[-1], t)
            prevMins.append(currMin)
        
        maxSub = nums[0]
        
        for i, t in enumerate(totals):
            maxSub = max(t, t - prevMins[i], maxSub)
    
        return maxSub
        

# [-2, 1]
# [-2,-1]
# [0, -2]
