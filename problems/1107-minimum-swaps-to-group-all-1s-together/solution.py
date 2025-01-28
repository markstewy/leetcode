class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = nums.count(1)
        window_ones = max_window_ones = 0

        l = 0
        for r in range(len(nums)):
            window_ones += nums[r]
            if r - l + 1 > total_ones:
                window_ones -= nums[l]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)

        return total_ones - max_window_ones
            

