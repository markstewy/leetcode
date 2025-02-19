class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = Counter(nums)
        perm = []

        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    perm.append(n)
                    helper()
                    perm.pop()
                    count[n] += 1
                
        helper()
        return ans
            
            
