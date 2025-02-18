class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = nums.count(1)
        nums = nums + nums
        oneCount = 0
        maxOneCount = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                oneCount += 1
            
            if r - l + 1 > windowSize:
                if nums[l] == 1:
                    oneCount -= 1
                l += 1

            maxOneCount = max(maxOneCount, oneCount)
    
        return windowSize - maxOneCount
