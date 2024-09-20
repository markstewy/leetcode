class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {} # num: idx

        for i, n in enumerate(nums):
            diff = target - n

            if diff in cache:
                return [i, cache[diff]]
            else:
                cache[n] = i
        return []
