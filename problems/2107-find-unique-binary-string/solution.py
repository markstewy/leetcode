class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k = len(nums)
        count = {"0": k, "1": k}
        numSet = set(nums)
        perm = []
        self.ans = None

        def helper():
            if len(perm) == k:
                if "".join(perm) not in numSet:
                    self.ans = "".join(perm)
                return
            
            for d in count:
                if count[d] > 0:
                    perm.append(d)
                    count[d] -= 1
                    helper()
                    count[d] += 1
                    perm.pop()
        helper()
        return self.ans
            

