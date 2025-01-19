class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxConsec = 0

        for n in numSet:
            if n - 1 not in numSet: # is a starting point
                l = 0
                while n + l in numSet:
                    l += 1
                    maxConsec = max(maxConsec, l)
        
        return maxConsec
