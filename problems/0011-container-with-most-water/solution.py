class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxWater = 0

        while l < r:
            length = r - l
            h = min (height[l], height[r])
            maxWater = max(maxWater, length * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maxWater
