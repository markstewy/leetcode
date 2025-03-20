class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = nums.count(1)
        nums = nums + nums[:windowSize]
        maxOnes = 0

        currCount = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                currCount += 1
            
            if r - l + 1 > windowSize:
                if nums[l] == 1:
                    currCount -= 1
                l += 1
            
            maxOnes = max(maxOnes, currCount)
        
        return windowSize - maxOnes
