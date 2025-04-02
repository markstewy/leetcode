class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        nset = set(nums)
        perm = []
        counts = {
            "0": len(nums),
            "1": len(nums)
        }
        self.ans = None

        def helper():
            if self.ans:
                return
            if len(perm) == len(nums):
                if "".join(perm) not in nset:
                    self.ans = "".join(perm)
                return
            
            for c in counts:
                if counts[c] > 0:
                    counts[c] -= 1
                    perm.append(c)
                    helper()
                    counts[c] += 1
                    perm.pop()
        
        helper()
        return self.ans
