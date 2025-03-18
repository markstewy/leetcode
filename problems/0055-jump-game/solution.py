class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIdx = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalIdx:
                goalIdx = i
        
        return goalIdx == 0
