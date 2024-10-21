class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)


        mxLength = 0
        for n in nSet:
            if n - 1 not in nSet:
                l = 0
                while n in nSet:
                    l += 1
                    n += 1
                    mxLength = max(mxLength, l)
        
        return mxLength
                
