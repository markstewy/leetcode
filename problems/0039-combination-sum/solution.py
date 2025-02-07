class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def helper(i: int, sub: [int], total: int) -> None:
            if i >= len(candidates) or total > target:
                return
            
            if total == target:
                self.ans.append(sub.copy())
                return

            sub.append(candidates[i])
            helper(i, sub, total + candidates[i])
            sub.pop()
            helper(i + 1, sub, total)
        
        helper(0, [], 0)
        return self.ans
