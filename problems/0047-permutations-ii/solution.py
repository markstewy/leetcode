class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        ans = []
        perm = []

        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    helper()
                    count[n] += 1
                    perm.pop()
        helper()
        return ans
        


