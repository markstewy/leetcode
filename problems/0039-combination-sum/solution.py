class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, sub, total):
            if total > target: return
            if total == target:
                ans.append(sub.copy())
                return
            for j in range(i, len(candidates)):
                sub.append(candidates[j])
                dfs(j, sub, total + candidates[j])
                sub.pop()
        dfs(0, [], 0)
        return ans
