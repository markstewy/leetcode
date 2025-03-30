class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def hasIndex():
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return True
            return False


        def firstIdx():
            l = 0
            r = len(nums) - 1
            closestPrev = -1

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] < target:
                    closestPrev = max(closestPrev, m)
                    l = m + 1
                elif nums[m] >= target:
                    r = m - 1
            
            return closestPrev + 1

        
        def lastIdx():
            l = 0
            r = len(nums) - 1
            closestNext = len(nums)

            while l <= r:
                m = l + (r - l) // 2
            
                if nums[m] > target:
                    closestNext = min(closestNext, m)
                    r = m - 1
                elif nums[m] <= target:
                    l += 1
            
            return closestNext - 1
        
        if not hasIndex():
            return [-1, -1]
        return [firstIdx(), lastIdx()]

