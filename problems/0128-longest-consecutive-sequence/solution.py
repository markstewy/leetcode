class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        mL = 0

        for n in nums:
            if n - 1 not in nSet:
                l = 0
                while n in nSet:
                    l += 1
                    n += 1
                mL = max(mL, l)
        
        return mL
                
