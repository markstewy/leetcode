class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for i, n in enumerate(nums):
            if nums[i] - 1 not in numSet: # this is a beginning of a sequence
                l = 1
                while n + l in numSet:
                    l += 1
                longest = max(longest, l)
        
        return longest



