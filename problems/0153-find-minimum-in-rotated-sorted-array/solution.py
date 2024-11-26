class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mn = float("infinity")

        while l <= r:
            m = l + (r - l) // 2
            mn = min(nums[m], mn)

            if nums[m] > nums[r]: # right side contians min
                l = m + 1
            else: # left side contains min
                r = m - 1
        
        return mn
            
