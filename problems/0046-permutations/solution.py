class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        numSet = set()

        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for n in nums:
                if n not in numSet:
                    numSet.add(n)
                    perm.append(n)
                    helper()
                    perm.pop()
                    numSet.remove(n)
        helper()
        return ans
