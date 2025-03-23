class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs():
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = l + (r - l) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return True
            return False
        
        def bsl():
            l = 0
            r = len(nums) - 1
            closestPrev = -1

            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    closestPrev = m
                    l = m + 1
                else:
                    r = m - 1
            
            return closestPrev + 1
        
        def bsr():
            l = 0
            r = len(nums) - 1
            closestNext = len(nums)

            while l <= r:
                m = l + (r - l) // 2
                if nums[m] > target:
                    r = m - 1
                    closestNext = m
                else:
                    l = m + 1
            
            return closestNext - 1
        
        if not bs():
            return [-1, -1]
        return [bsl(), bsr()]
