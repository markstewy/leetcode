class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def helper(i: int, sub: [int], total: int):
            if total == target:
                ans.append(sub.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            sub.append(candidates[i])
            helper(i + 1, sub, total + candidates[i])
            sub.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            helper(i + 1, sub, total)
        
        helper(0, [], 0)
        return ans

