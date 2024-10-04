class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        ml = 0

        for n in nums:
            if n - 1 not in nSet and n in nSet:
                l = 0
                while n + l in nSet:
                    l += 1
                ml = max(l, ml)
        return ml
