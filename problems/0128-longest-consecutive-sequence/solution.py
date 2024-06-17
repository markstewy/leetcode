class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0

        for n in numSet:
            if n - 1 not in numSet:
                l = 0
                while n in numSet:
                    l += 1
                    n += 1
                if ans < l:
                    ans = l
        
        return ans
