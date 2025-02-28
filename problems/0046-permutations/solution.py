class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        permSet = set()
        perm = []

        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for n in nums:
                if n not in permSet:
                    permSet.add(n)
                    perm.append(n)
                    helper()
                    perm.pop()
                    permSet.remove(n)
        
        helper()
        return ans
