class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(i, sub, total):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                ans.append(sub.copy())
                return
            
            helper(i + 1, sub, total)
            
            sub.append(candidates[i])
            helper(i, sub, total + candidates[i])
            sub.pop()
        
        helper(0, [], 0)
        return ans
