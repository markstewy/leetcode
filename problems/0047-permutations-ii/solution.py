class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        nCount = Counter(nums)

        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for n in nCount:
                if nCount[n] > 0:
                    perm.append(n)
                    nCount[n] -= 1
                    helper()
                    nCount[n] += 1
                    perm.pop()
        helper()
        return ans

