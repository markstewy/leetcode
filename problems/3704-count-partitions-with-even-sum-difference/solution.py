class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        count = 0

        for i in range(len(nums) - 1):
            l += nums[i]
            r -= nums[i]
            if (r - l) % 2 == 0:
                count += 1
        
        return count
