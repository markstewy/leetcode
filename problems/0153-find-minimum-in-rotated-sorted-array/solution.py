class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min will be in noncontinuous section

        l = 0
        r = len(nums) - 1
        mn = float("infinity")

        while l <= r:
            m = l + (r - l) // 2
            mn = min(mn, nums[m])

            if nums[r] < nums[m]: # contains the min
                l = m + 1
            else: # contians the min
                r = m - 1
        return mn

