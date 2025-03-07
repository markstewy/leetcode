class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        ans = []
        print(nums)

        def helper(sub, i):
            if len(sub) == k:
                ans.append(sub.copy())
                return
            if i >= len(nums):
                return
            
            sub.append(nums[i])
            helper(sub, i + 1)
            sub.pop()

            helper(sub, i + 1)
        
        helper([], 0)
        return ans

