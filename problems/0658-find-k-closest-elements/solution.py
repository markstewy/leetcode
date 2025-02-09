class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda n : abs(n - x))
        ans = arr[:k]
        ans.sort()
        return ans
