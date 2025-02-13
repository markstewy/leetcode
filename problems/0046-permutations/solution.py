class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums

        def helper(sub, subSet) -> None:
            if len(sub) == len(self.nums):
                self.ans.append(sub.copy())
                return
            
            for n in self.nums:
                if n not in subSet:
                    subSet.add(n)
                    sub.append(n)
                    helper(sub, subSet)
                    sub.pop()
                    subSet.remove(n)

        helper([], set())            
        return self.ans
