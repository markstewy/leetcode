class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(sub, subSet):
            if len(sub) == len(nums):
                ans.append(sub.copy())
                return
            
            for n in nums:
                if n not in subSet:
                    sub.append(n)
                    subSet.add(n)
                    helper(sub, subSet)
                    subSet.remove(n)
                    sub.pop()
        
        helper([], set())
        return ans
            
                
