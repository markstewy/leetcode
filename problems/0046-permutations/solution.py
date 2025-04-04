class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        count = Counter(nums)

        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    perm.append(c)
                    helper()
                    perm.pop()
                    count[c] += 1
                    
        
        helper()
        return ans
