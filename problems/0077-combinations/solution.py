class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(sub, i):
            if len(sub) == k:
                ans.append(sub.copy())
                return
            if i > n:
                return
            
            sub.append(i)
            helper(sub, i + 1)
            sub.pop()

            helper(sub, i + 1)
        
        helper([], 1)
        return ans
