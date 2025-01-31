class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = sum(nums)
        arrayLen = len(nums)

        count = 0
        maxCount = 0
        l = 0
        for r in range(arrayLen * 2):
            if r - l + 1 > windowSize:
                count -= nums[l % arrayLen]
                l += 1
            
            count += nums[r % arrayLen] 
            maxCount = max(count, maxCount)
        
        return windowSize - maxCount

