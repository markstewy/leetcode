class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ans = []

        def helper(i: int, sub: [int]) -> None:
            if i >= len(self.nums):
                self.ans.append(sub.copy())
                return
            
            helper(i + 1, sub)

            sub.append(self.nums[i])
            helper(i + 1, sub)
            sub.pop()
            
        helper(0, [])
        return self.ans
