class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []
        totalWater = 0

        m = 0
        for h in height:
            m = max(h, m)
            ltr.append(m)
        

        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(height[i], m)
            rtl.append(m)
        rtl.reverse()

        i = 1
        while i < len(height) - 1:
            waterLevel = min(ltr[i - 1], rtl[i + 1])
            floor = height[i]
            waterVolume = max(waterLevel - floor, 0)
            totalWater += waterVolume
            i += 1
        
        return totalWater

            
