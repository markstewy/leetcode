class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        subSet = set()

        def helper(sub, subSet):
            if len(sub) == len(nums):
                ans.append(sub.copy())
            
            for n in nums:
                if n not in subSet:
                    sub.append(n)
                    subSet.add(n)
                    helper(sub, subSet)
                    sub.pop()
                    subSet.remove(n)
        
        helper([], set())
        return ans

