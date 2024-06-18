class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = [], []
        totalWaterVol = 0

        m = 0
        for h in height:
            m = max(m, h)
            lmax.append(m)
        
        m = 0
        for i in range(len(height) - 1 , -1, -1):
            m = max(height[i], m)
            rmax.append(m)
        rmax.reverse()
    
        i = 1
        while i < len(height) - 1:
            waterlevel = min(lmax[i - 1], rmax[i + 1])
            groundlevel = height[i]
            waterdepth = max(waterlevel - groundlevel, 0)
            totalWaterVol += waterdepth
            i += 1
            
        return totalWaterVol
