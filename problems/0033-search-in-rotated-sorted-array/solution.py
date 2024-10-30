class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m

            # find the consecutive side
            if nums[l] <= nums[m]: # lower is consecutive
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # upper is consecutive
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
