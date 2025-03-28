class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReachIdxs = []
        maxReach = 0

        for i, n in enumerate(nums):
            maxReach = max(maxReach, i + n)
            maxReachIdxs.append(maxReach)
        
        prev = -1
        i = 0
        count = 0
        while i != prev:
            if i >= len(nums) - 1:
                return count
            
            prev = i
            i = maxReachIdxs[i]
            count += 1
        
        
