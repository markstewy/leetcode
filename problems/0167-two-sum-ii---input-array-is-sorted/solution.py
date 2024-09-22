class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l, r = 0, len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
        
