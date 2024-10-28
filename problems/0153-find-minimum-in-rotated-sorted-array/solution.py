class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = float("infinity")

        while l <= r:
            m = l + (r - l) // 2
            minimum = min(minimum, nums[l], nums[r], nums[m])

            if nums[m] > nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return minimum
