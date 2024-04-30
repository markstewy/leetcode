class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in cache:
                return [i, cache[diff]]
            
            cache[nums[i]] = i
