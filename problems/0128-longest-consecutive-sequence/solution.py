class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        maxLen = 0

        for n in nset:
            if n - 1 not in nset:
                l = 0
                while n + l in nset:
                    l += 1
                    maxLen = max(maxLen, l)
                
        return maxLen
