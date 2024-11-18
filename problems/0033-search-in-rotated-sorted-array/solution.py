class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            if nums[r] > nums[m]: # right side is ascending
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: # left side is ascending
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
                
            

