class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = [0 if n % 2 == 0 else 1 for n in nums]
        ans.sort()
        return ans
