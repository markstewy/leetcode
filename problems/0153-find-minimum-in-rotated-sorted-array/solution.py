class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = float("infinity")

        while l <= r:
            m = l + (r - l) // 2
            minVal = min(nums[m], minVal)

            if nums[m] < nums[r]: # right side is ascending and doesn't have the min
                r = m - 1
            else: # left side is ascending and doesn't have the min
                l = m + 1
        
        return minVal

