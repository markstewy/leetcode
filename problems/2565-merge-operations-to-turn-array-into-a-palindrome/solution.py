class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        sumCount = 0

        # [4,3,2,3,2,4,1]

        while l <= r:
            if l == r:
                break
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else:
                if nums[l] < nums[r]: # sum the left
                    nums[l + 1] += nums[l]
                    l += 1
                    sumCount += 1
                elif nums[l] > nums[r]: # sum the right
                    nums[r - 1] += nums[r]
                    r -= 1
                    sumCount += 1
        
        return sumCount
