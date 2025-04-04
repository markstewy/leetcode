class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        perm = []
        permSet = set()
        ans = []

        def helper():
            if len(perm) == len(nums):
                # if "".join(perm) not in permSet:
                ans.append(perm.copy())
                    # permSet.add("".join(perm))
                return
            
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    perm.append(c)
                    helper()
                    perm.pop()
                    count[c] += 1
        
        helper()
        return ans
