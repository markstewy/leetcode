class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k = len(nums)
        numSet = set(nums)
        numCount = {"0": k, "1": k}
        ans = None
        perm = []

        def helper():
            nonlocal ans
            if ans != None:
                return
            if len(perm) == k:
                if "".join(perm) not in numSet:
                    ans = "".join(perm)
                return
            
            for n in numCount:
                if numCount[n] > 0:
                    numCount[n] -= 1
                    perm.append(n)
                    helper()
                    perm.pop()
                    numCount[n] += 1
        
        helper()
        return ans

