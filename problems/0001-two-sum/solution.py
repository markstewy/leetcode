class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {} # n: idx

        for i, n in enumerate(nums):
            diff = target - n

            if diff in store:
                return [store[diff], i]
            
            store[n] = i
