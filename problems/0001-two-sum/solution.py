class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nToIdx = {} # n: idx

        for i, n in enumerate(nums):
            diff = target - n

            if diff in nToIdx:
                return [i, nToIdx[diff]]
            
            nToIdx[n] = i
        
        return []
