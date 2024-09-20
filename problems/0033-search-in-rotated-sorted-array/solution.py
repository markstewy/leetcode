class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            
            if nums[m] >= nums[0]:
                # we are on the left side continuous array
                if target >= nums[0] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # we are on the right side continuous array
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


# [4, 5, 6, 7, 1, 2, 3]
