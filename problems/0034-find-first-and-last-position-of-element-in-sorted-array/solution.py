class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def closestPrev():
            l = 0
            r = len(nums) - 1
            closestPrev = 0

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] <= target:
                    closestPrev = m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return closestPrev if nums[closestPrev] == target else closestPrev + 1

        
        def closestNext():
            l = 0
            r = len(nums) - 1
            closestNext = r

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] >= target:
                    closestNext = m
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return closestNext if nums[closestNext] == target else closestNext - 1
        
        if not nums or target not in nums:
            return [-1, -1]
        return [closestPrev(), closestNext()]
