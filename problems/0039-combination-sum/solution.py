class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(sub, i, total):
            if total == target:
                ans.append(sub.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            sub.append(candidates[i])
            helper(sub, i, total + candidates[i])
            sub.pop()

            helper(sub, i + 1, total)

        helper([], 0, 0)
        return ans

