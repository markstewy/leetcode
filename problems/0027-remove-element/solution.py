class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # temp = nums[j]
                nums[j] = nums[i]
                # nums[i] = temp
                j += 1
        
        return j

