class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {} # n: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in cache:
                return [i, cache[diff]]
            
            cache[n] = i
        
        return []
