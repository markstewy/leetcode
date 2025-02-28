class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []


        sub = []
        def helper(sub, i, total):
            if total == target:
                ans.append(sub.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            sub.append(candidates[i])
            helper(sub, i + 1, total + candidates[i])
            sub.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            helper(sub, i + 1, total)

        
        helper([], 0, 0)
        return ans
