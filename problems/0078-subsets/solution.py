class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums

        def helper(sub, i):
            if i == len(self.nums):
                self.ans.append(sub.copy())
                return
            
            helper(sub, i + 1)
            sub.append(self.nums[i])
            helper(sub, i + 1)
            sub.pop()
        
        helper([], 0)
        return self.ans

