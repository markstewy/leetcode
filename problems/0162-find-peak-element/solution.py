class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.peak = None
        self.nums = nums

        def helper(l, r):
            if self.peak:
                return
            if l == r:
                m = l
                lval = self.nums[m - 1] if m > 0 else self.nums[m] - 1
                rval = self.nums[m + 1] if m < len(self.nums) - 1 else self.nums[m] - 1
                if lval < self.nums[m] > rval:
                    self.peak = m
                return
            m = l + (r - l) // 2
            helper(l, m)
            helper(m + 1, r)
        
        helper(0, len(self.nums) - 1)
        return self.peak
        
