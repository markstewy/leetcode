class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        reach = []
        maxReach = 0

        for i, n in enumerate(nums):
            maxReach = max(maxReach, i + n)
            reach.append(maxReach)

        print(reach)
        
        count = 0
        i = 0
        while True:
            i = reach[i]
            count += 1
            if i >= len(nums) - 1:
                return count

