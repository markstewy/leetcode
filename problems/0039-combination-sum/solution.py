class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        candidates = list(set(candidates))
        ans = []

        def helper(sub, i , total):
            if total == target:
                ans.append(sub.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            sub.append(candidates[i])
            helper(sub, i, total + candidates[i])
            sub.pop()

            
            # while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
            #     i += 1

            helper(sub, i + 1, total)
        
        helper([], 0, 0)
        return ans
        
