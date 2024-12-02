class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = float("infinity")

        while l <= r:
            m = l + (r - l) // 2
            minVal = min(minVal, nums[m])

            if nums[m] < nums[r]: # right is the continuous side of the array, the min is on the other side
                r = m - 1
            else: # left is the continuous side of the array, min is on the other side
                l = m + 1
        return minVal


