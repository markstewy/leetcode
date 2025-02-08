class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def helper(i, sub, total):
            if total == target:
                ans.append(sub.copy())
                return
            if total > target or i >= len(candidates):
                return

            sub.append(candidates[i])
            helper(i + 1, sub, total + candidates[i])
            sub.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, sub, total)
        
        helper(0, [], 0)
        return ans
