class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {} # n: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in cache:
                return [i, cache[diff]]
            cache[n] = i
        
        return [-1, -1]
