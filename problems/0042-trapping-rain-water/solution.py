class Solution:
    def trap(self, height: List[int]) -> int:
        
        ltr, rtl = [], []

        mh = 0
        for h in height:
            mh = max(h, mh)
            ltr.append(mh)
        

        mh = 0
        for i in range(len(height) - 1, -1, -1):
            mh = max(height[i], mh)
            rtl.append(mh)
        rtl.reverse()
    
        totalVol = 0
        for i in range(1, len(height) - 1):
            waterDepth = min(ltr[i - 1], rtl[i + 1])
            floorDepth = height[i]
            waterVol = max(waterDepth - floorDepth, 0)
            totalVol += waterVol
    
        return totalVol
