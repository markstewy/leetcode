class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {} # key: n, val: idx
        for i, n in enumerate(nums):
            diff = target - n

            if diff in idxMap:
                return [idxMap[diff], i]
            else:
                idxMap[n] = i
