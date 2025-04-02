class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []        

        def helper(sub, i):
            if i >= len(nums):
                ans.append(sub.copy())
                return
            
            sub.append(nums[i])
            helper(sub, i + 1)
            sub.pop()

            helper(sub, i + 1)
    
        helper([], 0)
        return ans
