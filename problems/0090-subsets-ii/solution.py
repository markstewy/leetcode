class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def helper(sub, i):
            if i >= len(nums):
                ans.append(sub.copy())
                return
            
            sub.append(nums[i])
            helper(sub, i + 1)
            sub.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            helper(sub, i + 1)
        
        helper([], 0)
        return ans
