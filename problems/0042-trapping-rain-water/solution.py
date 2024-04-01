class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []
        waterTotal = 0

        m = 0
        for n in height:
            m = max(m, n)
            ltr.append(m)
        m = 0
        for i in range(len(height) - 1, -1 , -1):
            m = max(m, height[i])
            rtl.append(m)
        rtl.reverse()

        for i in range(1, len(height) - 1):
            water = min(ltr[i - 1], rtl[i + 1]) - height[i]
            waterTotal += max(0, water)
        
        return waterTotal

