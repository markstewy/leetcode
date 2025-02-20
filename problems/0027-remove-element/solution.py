class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertIdx = 0
        for i in range(len(nums)):
            nums[insertIdx] = nums[i]
            if nums[i] != val:
                insertIdx += 1
        
        return insertIdx
