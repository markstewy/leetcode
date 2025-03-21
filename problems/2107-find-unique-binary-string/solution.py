class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numSet = set(nums)
        k = len(nums)
        count = {"0": k, "1": k}
        perm = []
        self.ans = None

        def helper():
            if self.ans:
                return

            if len(perm) == k:
                if "".join(perm) not in numSet:
                    self.ans = "".join(perm)
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    perm.append(n)
                    helper()
                    perm.pop()
                    count[n] += 1
        
        helper()
        return self.ans
            

