class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxIdxReach = []
        reach = 0

        for i, n in enumerate(nums):
            reach = max(reach, n + i)
            maxIdxReach.append(reach)
        # print(maxIdxReach)
        
        idx = 0
        count = 0
        while True:
            if idx >= len(nums) - 1:
                break
            idx = maxIdxReach[idx]
            count += 1
        
        return count
            


                

