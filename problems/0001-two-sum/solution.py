class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {} #n -> i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in cache:
                return [cache[diff], i]
            else:
                cache[n] = i
        
        return [-1, -1]
