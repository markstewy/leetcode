class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binarySet = set(nums)
        k = len(nums[0])
        
        bitCount = {"0": k, "1": k}
        perm = []
        self.ans = None

        def helper():
            if self.ans != None:
                return
            if len(perm) == k and "".join(perm) not in binarySet:
                self.ans = "".join(perm)
                return
            
            for n in bitCount:
                if bitCount[n] > 0:
                    perm.append(n)
                    bitCount[n] -= 1
                    helper()
                    bitCount[n] += 1
                    perm.pop()
        
        helper()
        return self.ans
            
