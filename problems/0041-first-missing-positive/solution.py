class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0: # [1, 2, 3, 4] worst case ans is len(nums) + 1
                nums[i] = 0
        
        for n in nums:
            idx = abs(n) - 1
            if 0 <= idx < len(nums):
                if nums[idx] == 0:
                    nums[idx] = -(len(nums))
                else:
                    nums[idx] = -abs(nums[idx])
        
        for i , n in enumerate(nums):
            if n >= 0:
                return i + 1
        
        return len(nums) + 1
