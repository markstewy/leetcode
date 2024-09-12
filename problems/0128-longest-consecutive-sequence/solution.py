class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0

        for n in nums:
            if n - 1 not in numSet: # is start of sequence
                l = 0
                
                while n in numSet:
                    l += 1
                    n += 1
                
                ans = max(ans, l)
        return ans


