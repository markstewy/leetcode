class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for n in nums:            
            idx = abs(n) - 1
            if 0 <= idx < len(nums):
                if nums[idx] == 0:
                    nums[idx] = -(len(nums) + 1)
                else:
                    nums[idx] = -abs(nums[idx])
            
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1

            
        

