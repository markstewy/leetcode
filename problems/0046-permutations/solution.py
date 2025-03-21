class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nset = set()
        perm = []

        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for n in nums:
                if n not in nset:
                    nset.add(n)
                    perm.append(n)
                    helper()
                    perm.pop()
                    nset.remove(n)
        
        helper()
        return ans
