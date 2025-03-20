class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redCount = nums.count(0)
        whiteCount = nums.count(1)

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
        
        for r in range(l, len(nums)):
            if nums[r] == 1:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
        

            
