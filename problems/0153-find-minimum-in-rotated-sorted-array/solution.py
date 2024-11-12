class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = float("infinity")

        while l <= r:
            m = l + (r - l) // 2
            minVal = min(minVal, nums[m])

            if nums[m] > nums[r]: # right side is not ascending, min is on right
                l = m + 1
            else: # min is on left
                r = m - 1
        
        return minVal
