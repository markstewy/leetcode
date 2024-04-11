class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []
        totalWater = 0

        m = 0
        for n in height:
            m = max(m, n)
            ltr.append(m)

        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])
            rtl.append(m)
        rtl.reverse()
    
        # iterate over array excluding first and last positions (these can't hold water)
        i = 1
        while i < len(height) - 1:
            waterLevel = min(ltr[i - 1], rtl[i + 1])
            waterDepth = max(0, waterLevel - height[i])
            totalWater += waterDepth
            i += 1
        return totalWater


