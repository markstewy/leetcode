class Solution:
    def jump(self, nums: List[int]) -> int:
        maxIdxReach = []
        maxIdx = 0

        for i, n in enumerate(nums):
            maxIdx = max(maxIdx, n + i)
            maxIdxReach.append(maxIdx)
        
        print(maxIdxReach)
        i = 0
        count = 0
        while i < len(nums) - 1:
            count += 1
            i = maxIdxReach[i]

        return count

