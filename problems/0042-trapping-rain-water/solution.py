class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []

        mh = 0
        for h in height:
            mh = max(mh, h)
            ltr.append(mh)
        

        mh = 0
        for i in range(len(height) - 1, -1, -1):
            mh = max(mh, height[i])
            rtl.append(mh)
        rtl.reverse()

        totalWater = 0
        i = 1
        while i < len(height) - 1:
            h = min(ltr[i - 1], rtl[i + 1])
            depth = max(0, h - height[i])
            totalWater += depth
            i += 1
    
        return totalWater
