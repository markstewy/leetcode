class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        minVal = float("infinity"
        )
        while l <= r:
            m = l + (r - l) // 2

            if nums[r] < nums[m]: # min is on the right
                l = m + 1            
            else:               # min is on the left
                r = m - 1
            minVal = min(minVal, nums[m])
        
        return minVal

