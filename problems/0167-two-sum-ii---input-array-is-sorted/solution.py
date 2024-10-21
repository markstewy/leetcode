class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                return [l + 1, r + 1]
            
            if target > total:
                l += 1
            elif target < total:
                r -= 1
        
        return []
