class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nSet = set(nums)
        
        for i in range(len(nums)):
            if i not in nSet:
                return i
        return len(nums)
            
