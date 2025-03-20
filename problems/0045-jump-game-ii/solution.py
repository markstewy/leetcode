class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = []
        reach = 0

        for i, n in enumerate(nums):
            reach = max(reach, n + i)
            maxReach.append(reach)
        
        i = 0
        count = 0
        # print(maxReach)
        while i < len(nums) - 1:
            i = maxReach[i]
            count += 1
        
        return count
