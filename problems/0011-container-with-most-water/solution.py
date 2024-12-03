class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxVol = 0

        while l < r:
            vol = (r - l) * min(height[l], height[r])
            maxVol = max(maxVol, vol)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maxVol 
