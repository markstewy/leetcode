class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(i, sub):
            if i >= len(nums):
                ans.append(sub.copy())
                return 
            
            sub.append(nums[i])
            helper(i + 1, sub)
            sub.pop()

            helper(i + 1, sub)

        helper(0, [])
        return ans

