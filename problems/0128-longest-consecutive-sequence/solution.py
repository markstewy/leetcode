class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # constant time lookup
        maxL = 0

        for n in nums:
            # is it a start of a set?
            if n - 1 not in numSet:
                l = 0
                while n in numSet:
                    l += 1
                    n += 1
                maxL = max(maxL, l)
        return maxL

            # if yes, start counting and record max length


