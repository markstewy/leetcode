class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []
        totalWater = 0

        mx = 0
        for h in height:
            mx = max(mx, h)
            ltr.append(mx)
        
        mx = 0
        for i in range(len(height) - 1, -1, -1):
            mx = max(height[i], mx)
            rtl.append(mx)
        rtl.reverse()

        i = 1
        while i < len(height) - 1:
            wHeight = min(ltr[i - 1], rtl[i + 1])
            floor = height[i]
            water = max(0, wHeight - floor)
            totalWater += water
            i += 1

        return totalWater
            

            
            


