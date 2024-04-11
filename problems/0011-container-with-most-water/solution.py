class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxA = 0

        while l < r:
            a = min(height[l], height[r]) * (r - l)
            maxA = max(maxA, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxA

