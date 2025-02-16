class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums

        def helper(sub: [int], subSet: set) -> None:
            if len(sub) == len(self.nums):
                self.ans.append(sub.copy())
                return
            
            for n in self.nums:
                if n not in subSet:
                    subSet.add(n)
                    sub.append(n)
                    helper(sub, subSet)
                    subSet.remove(n)
                    sub.pop()
        
        helper([], set())
        return self.ans
                
                    


