class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        maxL = 0

        for n in nums:
            if n - 1 not in numSet:
                l = 0
                while n + l in numSet:
                    l += 1
                    maxL = max(maxL, l)
        return maxL
