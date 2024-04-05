class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []

        m = 0
        for n in height:
            m = max(m , n)
            ltr.append(m)

        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])
            rtl.append(m)
        rtl.reverse()

        waterTotal = 0

        for i in range(1, len(height) - 1):
            h = min(ltr[i - 1], rtl[i + 1])
            watercount = max(0, h - height[i])
            waterTotal += watercount

        return waterTotal    

        

