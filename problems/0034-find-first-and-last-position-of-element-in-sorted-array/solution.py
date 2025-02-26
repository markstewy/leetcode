class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def indexOf(target):
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
        
        def closestPrev(target):
            l = 0
            r = len(nums) - 1
            closestPrev = l

            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    closestPrev = m
                    l = m + 1
                else:
                    r = m - 1
            
            return closestPrev if nums[closestPrev] == target else closestPrev + 1

        def closestNext(target):
            l = 0
            r = len(nums) - 1
            closestNext = r

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] > target:
                    closestNext = m
                    r = m - 1
                else:
                    l = m + 1
            
            return closestNext if nums[closestNext] == target else closestNext - 1

        if not indexOf(target):
            return [-1, -1]
        return [closestPrev(target), closestNext(target)] 
