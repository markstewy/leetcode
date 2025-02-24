class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        count = {"0": len(nums), "1": len(nums)}
        numSet = set(nums)
        self.ans = None

        perm = []
        def helper():
            if len(perm) == len(nums) and "".join(perm) not in numSet:
                self.ans = "".join(perm)
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    helper()
                    count[n] += 1
                    perm.pop()
    
        helper()
        return self.ans


