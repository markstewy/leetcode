class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(l, len(nums)):
            if nums[i] == 0:
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l += 1
        
        for i in range(l, len(nums)):
            if nums[i] == 1:
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l += 1
