class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # find permutation of length k from bnums
        self.ans = None
        
        numSet = set(nums)
        k = len(nums)
        permCount = {"0": k, "1": k}
        perm = []

        def helper():
            if self.ans:
                return
            if len(perm) == k:
                if "".join(perm) not in numSet:
                    self.ans = "".join(perm)
                return
            
            for d in permCount:
                if permCount[d] > 0:
                    permCount[d] -= 1
                    perm.append(d)
                    helper()
                    perm.pop()
                    permCount[d] += 1
        
        helper()
        return self.ans
            
                



