class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(sub, i):
            if i >= len(nums):
                ans.append(sub.copy())
                return
            
            helper(sub, i + 1)
            sub.append(nums[i])
            helper(sub, i + 1)
            sub.pop()
        
        helper([], 0)
        return ans

