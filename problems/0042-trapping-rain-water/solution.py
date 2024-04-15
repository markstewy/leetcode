class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []

        m = 0
        for n in height:
            m = max(m, n)
            ltr.append(m)
        
        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])
            rtl.append(m)
        rtl.reverse()

        totalWater = 0
        i = 1
        while i < len(height) - 1:
            waterHeight = min(ltr[i - 1], rtl[i + 1])
            depth = max(0, waterHeight - height[i])
            totalWater += depth
            i += 1
        
        return totalWater


