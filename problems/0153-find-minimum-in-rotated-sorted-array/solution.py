class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = nums[0]

        while l < r:
            m = l + (r - l) // 2
            minVal = min(nums[l], nums[m], nums[r], minVal)

            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return minVal
