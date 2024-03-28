class Solution:
    def maxArea(self, height: List[int]) -> int:
        ltr, rtl = [], []
    
        mx = 0
        for n in height:
            mx = max(n, mx)
            ltr.append(mx)

        mx = 0
        for i in range(len(height) - 1, -1, -1):
            mx = max(mx, height[i])
            rtl.append(mx)
        rtl.reverse()
    
        maxWater = 0
        l = 0
        r = len(height) - 1
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            maxWater = max(water, maxWater)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater

                
