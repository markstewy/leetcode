class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i, n in enumerate(nums):
            if n - 1 not in numSet:
                # this is the beg of a sequence
                
                l = 0
                while n + l in numSet:
                    l += 1
                
                longest = max(longest, l)
        return longest

