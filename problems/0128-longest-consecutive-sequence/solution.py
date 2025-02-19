class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        ml = 0

        for n in nset:
            if n - 1 not in nset:
                i = 0
                while n + i in nset:
                    i += 1
                ml = max(ml, i)
        
        return ml
