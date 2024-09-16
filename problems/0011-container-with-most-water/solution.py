class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxWater = 0

        while l < r:
            water = min(height[l], height[r]) * (r - l)
            maxWater = max(water, maxWater)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
