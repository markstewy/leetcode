class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        i = 0
        while i < len(nums):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return -1

# 2, 2, 3, 3, 4, 4, 5
