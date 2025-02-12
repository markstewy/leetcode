class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(i, sub):
            if i == len(nums):
                ans.append(sub.copy())
                return
            
            helper(i + 1, sub)
            sub.append(nums[i])
            helper(i + 1, sub)
            sub.pop()
        
        helper(0, [])
        return ans



