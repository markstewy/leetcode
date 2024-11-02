class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []

        mx = 0
        for h in height:
            mx = max(mx, h)
            ltr.append(mx)

        mx = 0
        for i in range(len(height) - 1, -1, -1):
            mx = max(mx, height[i])
            rtl.append(mx)
        rtl.reverse()


        total = 0
        for i in range(1, len(height) - 1): #double check
            waterLevel = min(ltr[i - 1], rtl[i + 1])
            floor = height[i]
            vol = max(0, waterLevel - floor)
            total += vol
    
        return total
